import argparse
import csv
import json
import os
import pickle
import random
import re
import shutil
from dataclasses import dataclass

import numpy as np
from concurrent.futures import ProcessPoolExecutor, as_completed

from goc import goc
from features import features
from preprocess import preprocess
from classifier import classify
from progress import ProgressBar

DEFAULT_DATA_FOLDER   = "./data/"
DEFAULT_RESULTS_FOLDER = "./results/"
TEMP_DIR              = "./temp/"
DEFAULT_SAMPLE        = 200000

CACHE_FILE         = os.path.join(TEMP_DIR, "pairs_cache.json")
TEXTS_CACHE_FILE   = os.path.join(TEMP_DIR, "texts_cache.pkl")
FEATURES_CACHE_FILE = os.path.join(TEMP_DIR, "features_cache.npz")

_FUNC_DEF_PATTERN = re.compile(r"^(def\s+(\w+)\s*\()", re.MULTILINE)


@dataclass
class RunOptions:
    run_goc:             bool = True
    run_baseline:        bool = False
    run_keyword_baseline: bool = False
    run_jaccard:         bool = False
    show_errors:         bool = False
    reprocess:           bool = False


# ── Entry point ────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data",    default=DEFAULT_DATA_FOLDER,
                        help=f"Path to the data folder (default: {DEFAULT_DATA_FOLDER})")
    parser.add_argument("--results", default=DEFAULT_RESULTS_FOLDER,
                        help=f"Path to the results folder (default: {DEFAULT_RESULTS_FOLDER})")
    parser.add_argument("--poolc",   action="store_true",
                        help="Load data from the PoolC Hugging Face dataset")
    parser.add_argument("--sample",  type=int, default=DEFAULT_SAMPLE,
                        help=f"Number of pairs to sample when using --poolc (default: {DEFAULT_SAMPLE})")
    parser.add_argument("--no-goc",          action="store_true", help="Skip the GoC classifier")
    parser.add_argument("--baseline",        action="store_true", help="Run TF-IDF baseline")
    parser.add_argument("--keyword-baseline",action="store_true", help="Run keyword-only TF-IDF baseline")
    parser.add_argument("--jaccard",         action="store_true", help="Run Jaccard similarity baseline")
    parser.add_argument("--show-errors",     action="store_true", help="Print details for failed files")
    parser.add_argument("--reprocess",       action="store_true", help="Force reprocessing of cached data")
    args = parser.parse_args()

    opts = RunOptions(
        run_goc=not args.no_goc,
        run_baseline=args.baseline,
        run_keyword_baseline=args.keyword_baseline,
        run_jaccard=args.jaccard,
        show_errors=args.show_errors,
        reprocess=args.reprocess,
    )

    print("----------")
    if args.poolc:
        print(f"Dataset: PoolC (Hugging Face)")
        print(f"Sample size: {args.sample} pairs ({args.sample // 2} positive, {args.sample // 2} negative)")
    else:
        print(f"Dataset: {args.data}")
    print(f"Results folder: {args.results}")
    print("----------")

    if args.poolc:
        run_poolc(args.results, args.sample, opts)
    else:
        run_local(args.data, args.results, opts)


# ── Local folder mode (SemanticCloneBench) ────────────────────────────────────

def run_local(data_folder, results_folder, opts: RunOptions):
    py_files = [
        os.path.join(root, f)
        for root, _, files in os.walk(data_folder)
        for f in files if f.endswith(".py")
    ]

    print(f"Processing {len(py_files)} files")
    os.makedirs(TEMP_DIR, exist_ok=True)

    progress = ProgressBar(len(py_files), ["Loaded", "Skipped", "Errors"])
    error_log = []
    positive_pairs = []
    func_index = [0]

    try:
        with ProcessPoolExecutor() as executor:
            futures = {executor.submit(_process_file, fp): fp for fp in py_files}
            for future in as_completed(futures):
                filepath = futures[future]
                try:
                    result = future.result()
                    if result is None:
                        progress.update("Skipped")
                    else:
                        feat_a, feat_b, text_a, text_b = result
                        idx_a, idx_b = _save_pair(feat_a, feat_b, text_a, text_b, func_index)
                        positive_pairs.append((idx_a, idx_b))
                        progress.update("Loaded")
                except Exception as e:
                    if opts.show_errors:
                        error_log.append(f"  {filepath}: {e}")
                    progress.update("Errors")
    except KeyboardInterrupt:
        progress.finish()
        print("\nInterrupted. Exiting.")
        shutil.rmtree(TEMP_DIR, ignore_errors=True)
        return

    progress.finish()
    _print_errors(error_log, opts.show_errors)

    negative_pairs = _generate_negative_pairs(positive_pairs, func_index[0], len(positive_pairs))
    print(f"Generating {len(negative_pairs)} negative pairs")

    _run_classifiers(positive_pairs, negative_pairs, results_folder, opts)
    shutil.rmtree(TEMP_DIR, ignore_errors=True)


# ── PoolC (Hugging Face) mode ─────────────────────────────────────────────────

def run_poolc(results_folder, sample_size, opts: RunOptions):
    if not opts.reprocess and os.path.exists(CACHE_FILE):
        with open(CACHE_FILE) as f:
            cache = json.load(f)
        if cache.get("sample_size") == sample_size:
            positive_pairs = [tuple(p) for p in cache["positive_pairs"]]
            negative_pairs = [tuple(p) for p in cache["negative_pairs"]]
            print(f"Loaded from cache: {len(positive_pairs)} positive, {len(negative_pairs)} negative pairs")
            _run_classifiers(positive_pairs, negative_pairs, results_folder, opts)
            return
        print(f"Cache sample size mismatch ({cache.get('sample_size')} vs {sample_size}) — reprocessing")

    positive_pairs, negative_pairs = _process_poolc(sample_size, opts.show_errors)

    with open(CACHE_FILE, "w") as f:
        json.dump({"sample_size": sample_size,
                   "positive_pairs": positive_pairs,
                   "negative_pairs": negative_pairs}, f)

    _run_classifiers(positive_pairs, negative_pairs, results_folder, opts)


def _process_poolc(sample_size, show_errors):
    from datasets import load_dataset

    half = sample_size // 2
    print("Streaming PoolC dataset from Hugging Face...")
    dataset = load_dataset("PoolC/1-fold-clone-detection-600k-5fold", split="train", streaming=True)

    pairs_raw = []
    pos_count = neg_count = 0
    for row in dataset:
        if row["similar"] == 1 and pos_count < half:
            pairs_raw.append((row["code1"], row["code2"], 1))
            pos_count += 1
        elif row["similar"] == 0 and neg_count < half:
            pairs_raw.append((row["code1"], row["code2"], 0))
            neg_count += 1
        if pos_count >= half and neg_count >= half:
            break

    print(f"Sampled {len(pairs_raw)} pairs — processing")
    os.makedirs(TEMP_DIR, exist_ok=True)

    progress = ProgressBar(len(pairs_raw), ["Loaded", "Errors"])
    error_log = []
    labeled_pairs = []
    texts = {}
    feature_vecs = {}
    func_index = [0]

    try:
        with ProcessPoolExecutor() as executor:
            futures = {
                executor.submit(_process_pair, code1, code2): (i, label)
                for i, (code1, code2, label) in enumerate(pairs_raw)
            }
            for future in as_completed(futures):
                i, label = futures[future]
                try:
                    feat_a, feat_b, text_a, text_b = future.result()
                    idx_a, idx_b = _save_pair(feat_a, feat_b, text_a, text_b, func_index)
                    texts[idx_a] = text_a
                    texts[idx_b] = text_b
                    feature_vecs[idx_a] = feat_a
                    feature_vecs[idx_b] = feat_b
                    labeled_pairs.append((idx_a, idx_b, label))
                    progress.update("Loaded")
                except Exception as e:
                    if show_errors:
                        error_log.append(f"  pair {i}: {e}")
                    progress.update("Errors")
    except KeyboardInterrupt:
        progress.finish()
        print("\nInterrupted. Exiting.")
        shutil.rmtree(TEMP_DIR, ignore_errors=True)
        raise SystemExit

    progress.finish()
    _print_errors(error_log, show_errors)

    positive_pairs = [(a, b) for a, b, lbl in labeled_pairs if lbl == 1]
    negative_pairs = [(a, b) for a, b, lbl in labeled_pairs if lbl == 0]
    print(f"Processed: {len(positive_pairs)} positive, {len(negative_pairs)} negative pairs")

    with open(TEXTS_CACHE_FILE, "wb") as f:
        pickle.dump(texts, f)
    np.savez(FEATURES_CACHE_FILE, **{str(k): v for k, v in feature_vecs.items()})

    return positive_pairs, negative_pairs


# ── Classifiers and comparisons ───────────────────────────────────────────────

def _run_classifiers(positive_pairs, negative_pairs, results_folder, opts: RunOptions):
    from baseline import baseline
    from jaccard_baseline import jaccard_baseline

    goc_results      = classify(positive_pairs, negative_pairs, TEMP_DIR, results_folder)      if opts.run_goc             else None
    full_tfidf       = baseline(positive_pairs, negative_pairs, TEMP_DIR, results_folder)      if opts.run_baseline        else None
    keyword_tfidf    = baseline(positive_pairs, negative_pairs, TEMP_DIR, results_folder, keyword_only=True) if opts.run_keyword_baseline else None
    jaccard_results  = jaccard_baseline(positive_pairs, negative_pairs, TEMP_DIR, results_folder) if opts.run_jaccard      else None

    comparisons = [
        (goc_results,   full_tfidf,      "GoC",          "TF-IDF (full)",          "statistical_comparison.csv"),
        (goc_results,   keyword_tfidf,   "GoC",          "TF-IDF (keywords only)", "statistical_comparison_keyword.csv"),
        (goc_results,   jaccard_results, "GoC",          "Jaccard",                "statistical_comparison_jaccard.csv"),
        (full_tfidf,    keyword_tfidf,   "TF-IDF (full)","TF-IDF (keywords only)", "statistical_comparison_tfidf_vs_keyword.csv"),
    ]

    for results_a, results_b, label_a, label_b, filename in comparisons:
        if results_a is not None and results_b is not None:
            print(f"\n{label_a} vs {label_b}:")
            _statistical_comparison(results_a, results_b, label_a, label_b, results_folder, filename)


def _statistical_comparison(results_a, results_b, label_a, label_b, results_folder, filename):
    from scipy.stats import wilcoxon, norm

    f1_a = np.array([r[3] for r in results_a])
    f1_b = np.array([r[3] for r in results_b])

    print(f"\n  --- Statistical Comparison (Wilcoxon Signed-Rank Test) ---")
    print(f"  {label_a} avg F1: {np.mean(f1_a):.4f}")
    print(f"  {label_b} avg F1: {np.mean(f1_b):.4f}")

    stat = p_value = effect_r = None
    try:
        stat, p_value = wilcoxon(f1_a, f1_b, alternative='two-sided')
        z = abs(norm.ppf(p_value / 2))
        effect_r = z / np.sqrt(len(f1_a))
        print(f"  W={stat:.4f}, p={p_value:.4f}, effect size r={effect_r:.4f}")
        if p_value < 0.05:
            better = label_a if np.mean(f1_a) > np.mean(f1_b) else label_b
            print(f"  Statistically significant (p<0.05) — {better} is better")
        else:
            print(f"  No statistically significant difference (p={p_value:.4f} >= 0.05)")
    except Exception as e:
        print(f"  Wilcoxon test failed: {e}")

    os.makedirs(results_folder, exist_ok=True)
    output_path = os.path.join(results_folder, filename)
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["fold", f"{label_a}_f1", f"{label_b}_f1", "difference"])
        for (fold, *_, fa), (_, *_, fb) in zip(results_a, results_b):
            writer.writerow([fold, f"{fa:.4f}", f"{fb:.4f}", f"{fa - fb:.4f}"])
        writer.writerow([])
        writer.writerow(["metric", "value"])
        writer.writerow([f"{label_a}_avg_f1", f"{np.mean(f1_a):.4f}"])
        writer.writerow([f"{label_b}_avg_f1", f"{np.mean(f1_b):.4f}"])
        if stat is not None:
            writer.writerow(["wilcoxon_W",    f"{stat:.4f}"])
            writer.writerow(["p_value",       f"{p_value:.4f}"])
            writer.writerow(["effect_size_r", f"{effect_r:.4f}"])
    print(f"  Saved to {output_path}")


# ── Processing helpers ─────────────────────────────────────────────────────────

def _process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        source = preprocess(f.read())
    matches = list(_FUNC_DEF_PATTERN.finditer(source))
    functions_by_name = {}
    for match in matches:
        name = match.group(2)
        functions_by_name.setdefault(name, []).append(match.start())
    for positions in functions_by_name.values():
        if len(positions) == 2:
            clone_a = _extract_function(source, positions[0], matches)
            clone_b = _extract_function(source, positions[1], matches)
            return features(goc(clone_a)), features(goc(clone_b)), clone_a, clone_b
    return None


def _process_pair(code1, code2):
    src1, src2 = preprocess(code1), preprocess(code2)
    return features(goc(src1)), features(goc(src2)), src1, src2


def _extract_function(source, start_pos, all_matches):
    for match in all_matches:
        if match.start() > start_pos:
            return source[start_pos:match.start()].rstrip()
    return source[start_pos:].rstrip()


def _save_pair(feat_a, feat_b, text_a, text_b, func_index):
    idx_a, idx_b = func_index[0], func_index[0] + 1
    func_index[0] += 2
    np.save(os.path.join(TEMP_DIR, f"func_{idx_a}.npy"), feat_a)
    np.save(os.path.join(TEMP_DIR, f"func_{idx_b}.npy"), feat_b)
    for idx, text in ((idx_a, text_a), (idx_b, text_b)):
        with open(os.path.join(TEMP_DIR, f"func_{idx}.txt"), "w", encoding="utf-8") as f:
            f.write(text)
    return idx_a, idx_b


def _generate_negative_pairs(positive_pairs, total_funcs, count):
    positive_set = {(min(a, b), max(a, b)) for a, b in positive_pairs}
    negative_pairs = []
    attempts = 0
    while len(negative_pairs) < count and attempts < count * 20:
        idx_a = random.randrange(0, total_funcs)
        idx_b = random.randrange(0, total_funcs)
        if idx_a != idx_b \
                and (idx_a // 2 != idx_b // 2) \
                and (min(idx_a, idx_b), max(idx_a, idx_b)) not in positive_set:
            negative_pairs.append((idx_a, idx_b))
        attempts += 1
    return negative_pairs


def _print_errors(error_log, show_errors):
    if show_errors and error_log:
        print("Errors:")
        for entry in error_log:
            print(entry)


if __name__ == "__main__":
    main()
