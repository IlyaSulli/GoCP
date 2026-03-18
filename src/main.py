import argparse
import json
import os
import random
import re
import shutil
import numpy as np
from concurrent.futures import ProcessPoolExecutor, as_completed

from goc import goc
from features import features
from preprocess import preprocess
from classifier import classify
from progress import ProgressBar

DEFAULT_DATA_FOLDER = "./data/"
DEFAULT_RESULTS_FOLDER = "./results/"
TEMP_DIR = "./temp/"
DEFAULT_SAMPLE = 10000
CACHE_FILE = os.path.join(TEMP_DIR, "pairs_cache.json")

_FUNC_DEF_PATTERN = re.compile(r"^(def\s+(\w+)\s*\()", re.MULTILINE)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default=DEFAULT_DATA_FOLDER,
                        help=f"Path to the data folder (default: {DEFAULT_DATA_FOLDER})")
    parser.add_argument("--results", default=DEFAULT_RESULTS_FOLDER,
                        help=f"Path to the results folder (default: {DEFAULT_RESULTS_FOLDER})")
    parser.add_argument("--poolc", action="store_true",
                        help="Load data from the PoolC Hugging Face dataset instead of a local folder")
    parser.add_argument("--sample", type=int, default=DEFAULT_SAMPLE,
                        help=f"Number of pairs to sample when using --poolc (default: {DEFAULT_SAMPLE})")
    parser.add_argument("--show-errors", action="store_true",
                        help="Display error details for each failed file")
    parser.add_argument("--baseline", action="store_true",
                        help="Run TF-IDF baseline classifier for comparison")
    parser.add_argument("--no-goc", action="store_true",
                        help="Skip the GoC classifier")
    parser.add_argument("--reprocess", action="store_true",
                        help="Force reprocessing even if cached data exists (--poolc only)")
    args = parser.parse_args()

    print(f"----------")
    if args.poolc:
        print(f"Dataset: PoolC (Hugging Face)")
        print(f"Sample size: {args.sample} pairs ({args.sample // 2} positive, {args.sample // 2} negative)")
    else:
        print(f"Dataset: {args.data}")
    print(f"Results folder: {args.results}")
    print(f"----------")

    if args.poolc:
        run_poolc(args.results, args.sample,
                  show_errors=args.show_errors,
                  run_goc=not args.no_goc,
                  run_baseline=args.baseline,
                  reprocess=args.reprocess)
    else:
        run_local(args.data, args.results,
                  show_errors=args.show_errors,
                  run_goc=not args.no_goc,
                  run_baseline=args.baseline)


# ── Local folder mode (SemanticCloneBench) ────────────────────────────────────

def run_local(data_folder, results_folder, show_errors=False, run_goc=True, run_baseline=False):
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
                    if show_errors:
                        error_log.append(f"  {filepath}: {e}")
                    progress.update("Errors")

    except KeyboardInterrupt:
        progress.finish()
        print("\nInterrupted by user. Exiting.")
        shutil.rmtree(TEMP_DIR, ignore_errors=True)
        return

    progress.finish()

    if show_errors and error_log:
        print("Errors:")
        for entry in error_log:
            print(entry)

    num_positive = len(positive_pairs)
    print(f"Generating {num_positive} negative pairs")
    negative_pairs = _generate_negative_pairs(positive_pairs, func_index[0], num_positive)

    _run_classifiers(positive_pairs, negative_pairs, results_folder, run_goc, run_baseline)
    shutil.rmtree(TEMP_DIR, ignore_errors=True)


# ── PoolC (Hugging Face) mode ─────────────────────────────────────────────────

def run_poolc(results_folder, sample_size, show_errors=False, run_goc=True, run_baseline=False, reprocess=False):
    if not reprocess and os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            cache = json.load(f)
        if cache.get("sample_size") == sample_size:
            positive_pairs = [tuple(p) for p in cache["positive_pairs"]]
            negative_pairs = [tuple(p) for p in cache["negative_pairs"]]
            print(f"Loaded from cache: {len(positive_pairs)} positive, {len(negative_pairs)} negative pairs")
            _run_classifiers(positive_pairs, negative_pairs, results_folder, run_goc, run_baseline)
            return
        print(f"Cache sample size mismatch ({cache.get('sample_size')} vs {sample_size}) — reprocessing")

    positive_pairs, negative_pairs = _process_poolc(sample_size, show_errors)

    with open(CACHE_FILE, "w") as f:
        json.dump({
            "sample_size": sample_size,
            "positive_pairs": positive_pairs,
            "negative_pairs": negative_pairs,
        }, f)

    _run_classifiers(positive_pairs, negative_pairs, results_folder, run_goc, run_baseline)


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
                    labeled_pairs.append((idx_a, idx_b, label))
                    progress.update("Loaded")
                except Exception as e:
                    if show_errors:
                        error_log.append(f"  pair {i}: {e}")
                    progress.update("Errors")

    except KeyboardInterrupt:
        progress.finish()
        print("\nInterrupted by user. Exiting.")
        shutil.rmtree(TEMP_DIR, ignore_errors=True)
        raise SystemExit

    progress.finish()

    if show_errors and error_log:
        print("Errors:")
        for entry in error_log:
            print(entry)

    positive_pairs = [(a, b) for a, b, lbl in labeled_pairs if lbl == 1]
    negative_pairs = [(a, b) for a, b, lbl in labeled_pairs if lbl == 0]
    print(f"Processed: {len(positive_pairs)} positive, {len(negative_pairs)} negative pairs")
    return positive_pairs, negative_pairs


# ── Shared helpers ─────────────────────────────────────────────────────────────

def _run_classifiers(positive_pairs, negative_pairs, results_folder, run_goc, run_baseline):
    if run_goc:
        print("Running GoC classifier...")
        classify(positive_pairs, negative_pairs, TEMP_DIR, results_folder)
    if run_baseline:
        from baseline import baseline
        print("Running TF-IDF baseline...")
        baseline(positive_pairs, negative_pairs, TEMP_DIR, results_folder)


def _process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        source = preprocess(f.read())
    matches = list(_FUNC_DEF_PATTERN.finditer(source))
    functions_by_name = {}
    for match in matches:
        name = match.group(2)
        if name not in functions_by_name:
            functions_by_name[name] = []
        functions_by_name[name].append(match.start())
    for positions in functions_by_name.values():
        if len(positions) == 2:
            clone_a = _extract_function(source, positions[0], matches)
            clone_b = _extract_function(source, positions[1], matches)
            return features(goc(clone_a)), features(goc(clone_b)), clone_a, clone_b
    return None


def _process_pair(code1, code2):
    src1 = preprocess(code1)
    src2 = preprocess(code2)
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
    with open(os.path.join(TEMP_DIR, f"func_{idx_a}.txt"), "w", encoding="utf-8") as f:
        f.write(text_a)
    with open(os.path.join(TEMP_DIR, f"func_{idx_b}.txt"), "w", encoding="utf-8") as f:
        f.write(text_b)
    return idx_a, idx_b


def _generate_negative_pairs(positive_pairs, total_funcs, count):
    positive_set = set(map(tuple, positive_pairs))
    negative_pairs = []
    attempts = 0
    while len(negative_pairs) < count and attempts < count * 20:
        idx_a = random.randrange(0, total_funcs)
        idx_b = random.randrange(0, total_funcs)
        same_file = (idx_a // 2 == idx_b // 2)
        already_used = (min(idx_a, idx_b), max(idx_a, idx_b)) in positive_set
        if idx_a != idx_b and not same_file and not already_used:
            negative_pairs.append((idx_a, idx_b))
        attempts += 1
    return negative_pairs


if __name__ == "__main__":
    main()
