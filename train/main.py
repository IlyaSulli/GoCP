import logging
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import argparse
import csv
import json
import pickle
import random
import re
import shutil
from dataclasses import dataclass

import numpy as np
from concurrent.futures import ProcessPoolExecutor, as_completed

from progress import Pipeline, ProgressBar

logger = logging.getLogger(__name__)


def _worker_init():
    # Worker processes don't inherit the main process's log handlers.
    # Silence logging and stderr entirely — exceptions surface via future.result().
    logging.disable(logging.CRITICAL)
    sys.stderr = open(os.devnull, "w")


def _setup_logging(results_folder: str, log_path: str = "") -> None:
    """Write INFO+ log messages to a file for the duration of the run.

    If log_path is empty, defaults to <results_folder>/gocp.log.
    """
    path = log_path if log_path else os.path.join(results_folder, "gocp.log")
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(levelname)-8s  %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.FileHandler(path, encoding="utf-8")],
        force=True,
    )
    logger.info("Logging initialised — output: %s", path)


_BANNER = (
    "\n\n"
    " ██████╗  ██████╗  ██████╗\n"
    "██╔════╝ ██╔═══██╗██╔════╝\n"
    "██║  ███╗██║   ██║██║\n"
    "██║   ██║██║   ██║██║\n"
    "╚██████╔╝╚██████╔╝╚██████╗\n"
    " ╚═════╝  ╚═════╝  ╚═════╝\n"
    "        · Python ·"
)

DEFAULT_DATA_FOLDER    = "./data/"
DEFAULT_RESULTS_FOLDER = "./results/"
DEFAULT_MODELS_FOLDER  = "./models/"
TEMP_DIR               = "./temp/"
DEFAULT_SAMPLE         = 20000

CACHE_FILE          = os.path.join(TEMP_DIR, "pairs_cache.json")
TEXTS_CACHE_FILE    = os.path.join(TEMP_DIR, "texts_cache.pkl")
FEATURES_CACHE_FILE = os.path.join(TEMP_DIR, "features_cache.npz")

_FUNC_DEF_PATTERN = re.compile(r"^(def\s+(\w+)\s*\()", re.MULTILINE)


@dataclass
class RunOptions:
    run_goc:            bool  = True
    run_tfidf:          bool  = False
    run_tfidf_keywords: bool  = False
    run_jaccard:        bool  = False
    show_errors:        bool  = False
    reprocess:          bool  = False
    save_models:        bool  = False
    fixed_threshold:    bool  = False
    log_path:           str | None = None   # None = no logging; "" = default path
    diverse_neg_ratio:  float = 0.0         # fraction of negatives drawn from CodeSearchNet

# ── Entry point ────────────────────────────────────────────────────────────────

def main():
    print(_BANNER)
    print()
    parser = argparse.ArgumentParser(
        description="Train and evaluate GoCP clone detection models.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "examples:\n"
            "  python train/main.py --poolc --sample 200000 --save-models\n"
            "  python train/main.py --poolc --sample 200000 --save-models --tfidf --tfidf-keywords --jaccard\n"
            "  python train/main.py --data ./data --save-models --fixed-threshold\n"
        ),
    )

    data_group = parser.add_argument_group("data source")
    data_group.add_argument("--data", metavar="DIR", default=DEFAULT_DATA_FOLDER,
                            help=f"path to local data folder (default: {DEFAULT_DATA_FOLDER})")
    data_group.add_argument("--poolc", action="store_true",
                            help="load data from the PoolC Hugging Face dataset instead of --data")
    data_group.add_argument("--sample", "-n", metavar="N", type=int, default=DEFAULT_SAMPLE,
                            help=f"number of pairs to sample from PoolC (default: {DEFAULT_SAMPLE})")

    methods_group = parser.add_argument_group("methods")
    methods_group.add_argument("--no-goc", action="store_true",
                               help="skip the GoCP classifier")
    methods_group.add_argument("--tfidf", action="store_true",
                               help="run TF-IDF (full tokens) comparison")
    methods_group.add_argument("--tfidf-keywords", action="store_true",
                               help="run TF-IDF (keywords only) comparison")
    methods_group.add_argument("--jaccard", action="store_true",
                               help="run Jaccard similarity baseline")

    output_group = parser.add_argument_group("output")
    output_group.add_argument("--results", "-r", metavar="DIR", default=DEFAULT_RESULTS_FOLDER,
                              help=f"path to results folder (default: {DEFAULT_RESULTS_FOLDER})")
    output_group.add_argument("--models", "-m", metavar="DIR", default=DEFAULT_MODELS_FOLDER,
                              help=f"path to models folder (default: {DEFAULT_MODELS_FOLDER})")
    output_group.add_argument("--save-models", action="store_true",
                              help="save trained models to --models")

    misc_group = parser.add_argument_group("misc")
    misc_group.add_argument("--fixed-threshold", action="store_true",
                            help="use a fixed 0.5 decision threshold instead of learning it from the validation set")
    misc_group.add_argument("--reprocess", action="store_true",
                            help="ignore cached data and reprocess from scratch")
    misc_group.add_argument("--show-errors", "-v", action="store_true",
                            help="print details for files that failed to process")
    misc_group.add_argument("--log", metavar="FILE", nargs="?", const="", default=None,
                            help="write a log file; FILE defaults to <results>/gocp.log")
    misc_group.add_argument("--diverse-negatives", metavar="RATIO", type=float,
                            nargs="?", const=0.7, default=0.0,
                            help="fraction of negatives drawn from CodeSearchNet (general Python) "
                                 "rather than PoolC; reduces same-domain bias (default when flag is given: 0.7)")

    args = parser.parse_args()

    opts = RunOptions(
        run_goc=not args.no_goc,
        run_tfidf=args.tfidf,
        run_tfidf_keywords=args.tfidf_keywords,
        run_jaccard=args.jaccard,
        show_errors=args.show_errors,
        reprocess=args.reprocess,
        save_models=args.save_models,
        fixed_threshold=args.fixed_threshold,
        log_path=args.log,
        diverse_neg_ratio=args.diverse_negatives,
    )

    models_folder = args.models if opts.save_models else None

    if args.poolc:
        run_poolc(args.results, models_folder, args.sample, opts)
    else:
        run_local(args.data, args.results, models_folder, opts)


# ── Local folder mode (SemanticCloneBench) ────────────────────────────────────

def run_local(data_folder, results_folder, models_folder, opts: RunOptions):
    if opts.log_path is not None:
        _setup_logging(results_folder, opts.log_path)
    logger.info("run_local: data=%s  results=%s", data_folder, results_folder)
    py_files = [
        os.path.join(root, f)
        for root, _, files in os.walk(data_folder)
        for f in files if f.endswith(".py")
    ]

    os.makedirs(TEMP_DIR, exist_ok=True)

    steps = ["Load local dataset"]
    if opts.run_goc:
        steps.append("Train GoCP")
    if opts.run_tfidf:
        steps.append("Train TF-IDF (Full)")
    if opts.run_tfidf_keywords:
        steps.append("Train TF-IDF (Keywords)")
    if opts.run_jaccard:
        steps.append("Train Jaccard")

    pipeline = Pipeline(steps)
    pipeline.begin("Load local dataset", len(py_files), ["Loaded", "Errors"])
    pipeline.status(f"Loading {len(py_files)} Python files...")

    error_log = []
    positive_pairs = []
    func_index = [0]

    try:
        with ProcessPoolExecutor(initializer=_worker_init) as executor:
            futures = {executor.submit(_process_file, fp): fp for fp in py_files}
            for future in as_completed(futures):
                filepath = futures[future]
                try:
                    result = future.result()
                    if result is None:
                        pipeline.update("Loaded")
                    else:
                        feat_a, feat_b, text_a, text_b = result
                        idx_a, idx_b = _save_pair(feat_a, feat_b, text_a, text_b, func_index)
                        positive_pairs.append((idx_a, idx_b))
                        pipeline.update("Loaded")
                except Exception as e:
                    if opts.show_errors:
                        error_log.append(f"  {filepath}: {e}")
                    pipeline.update("Errors")
    except KeyboardInterrupt:
        pipeline.finish()
        pipeline.complete()
        print("\nInterrupted. Exiting.")
        shutil.rmtree(TEMP_DIR, ignore_errors=True)
        return

    pipeline.finish()

    negative_pairs = _generate_negative_pairs(positive_pairs, func_index[0], len(positive_pairs))

    # In local mode all negatives come from the same source, so poolc_negative_pairs = negative_pairs
    results = _run_classifiers(positive_pairs, negative_pairs, negative_pairs,
                               results_folder, models_folder, opts, pipeline)

    pipeline.complete()

    dataset_info = [
        f"Dataset: {data_folder}",
        f"Files processed: {len(py_files)}",
        f"Positive pairs: {len(positive_pairs)}  Negative pairs: {len(negative_pairs)}",
    ]
    _print_summary(dataset_info, results, results_folder, models_folder)

    if opts.show_errors and error_log:
        print("Errors:")
        for entry in error_log:
            print(entry)

    _run_comparisons(results, results_folder)
    shutil.rmtree(TEMP_DIR, ignore_errors=True)


# ── PoolC (Hugging Face) mode ─────────────────────────────────────────────────

def run_poolc(results_folder, models_folder, sample_size, opts: RunOptions):
    if opts.log_path is not None:
        _setup_logging(results_folder, opts.log_path)
    logger.info("run_poolc: sample_size=%d  results=%s", sample_size, results_folder)
    using_cache = False
    cache = None
    diverse_neg_ratio = opts.diverse_neg_ratio
    if not opts.reprocess and os.path.exists(CACHE_FILE):
        with open(CACHE_FILE) as f:
            cache = json.load(f)
        if (cache.get("sample_size") == sample_size
                and cache.get("diverse_neg_ratio", 0.0) == diverse_neg_ratio):
            using_cache = True
        else:
            logger.info("Cache mismatch (sample_size or diverse_neg_ratio changed) — reprocessing")

    steps = []
    if not using_cache:
        steps.append("Stream PoolC dataset")
        if diverse_neg_ratio > 0:
            steps.append("Stream CodeSearchNet")
    if opts.run_goc:
        steps.append("Train GoCP")
    if opts.run_tfidf:
        steps.append("Train TF-IDF (Full)")
    if opts.run_tfidf_keywords:
        steps.append("Train TF-IDF (Keywords)")
    if opts.run_jaccard:
        steps.append("Train Jaccard")

    pipeline = Pipeline(steps)

    error_count = 0
    error_log   = []
    if using_cache:
        positive_pairs       = [tuple(p) for p in cache["positive_pairs"]]
        poolc_negative_pairs = [tuple(p) for p in cache["poolc_negative_pairs"]]
        csn_negative_pairs   = [tuple(p) for p in cache.get("csn_negative_pairs", [])]
        if not positive_pairs and not poolc_negative_pairs and not csn_negative_pairs:
            print("Cached pair lists are empty — run with --reprocess to rebuild from scratch.")
            return
    else:
        positive_pairs, poolc_negative_pairs, csn_negative_pairs, error_count, error_log = _process_poolc(
            sample_size, pipeline, diverse_neg_ratio
        )
        if positive_pairs or poolc_negative_pairs or csn_negative_pairs:
            with open(CACHE_FILE, "w") as f:
                json.dump({"sample_size": sample_size,
                           "diverse_neg_ratio": diverse_neg_ratio,
                           "positive_pairs": positive_pairs,
                           "poolc_negative_pairs": poolc_negative_pairs,
                           "csn_negative_pairs": csn_negative_pairs}, f)
        else:
            print("No pairs were processed successfully — check --show-errors for details.")
            return

    # GoCP trains on all negatives; text-based baselines use PoolC-only negatives
    # to avoid domain-mixing artifacts in TF-IDF vocabulary.
    all_negative_pairs = poolc_negative_pairs + csn_negative_pairs
    results = _run_classifiers(positive_pairs, all_negative_pairs, poolc_negative_pairs,
                               results_folder, models_folder, opts, pipeline)

    pipeline.complete()

    if opts.show_errors and error_log:
        print("Errors:")
        for entry in error_log:
            print(entry)

    half = sample_size // 2
    if diverse_neg_ratio > 0:
        poolc_neg = int(half * (1 - diverse_neg_ratio))
        csn_neg   = half - poolc_neg
        dataset_info = [
            f"Dataset:     PoolC + CodeSearchNet (Hugging Face)",
            f"Sample size: {sample_size} pairs  ({half} positive, {poolc_neg} PoolC neg + {csn_neg} CSN neg)",
        ]
    else:
        dataset_info = [
            f"Dataset:     PoolC (Hugging Face)",
            f"Sample size: {sample_size} pairs  ({half} positive, {half} negative)",
        ]
    if error_count:
        real_total = len(positive_pairs) + len(poolc_negative_pairs) + len(csn_negative_pairs)
        dataset_info.append(f"Processed:   {real_total} pairs  ({error_count} failed)")

    _print_summary(dataset_info, results, results_folder, models_folder)
    _run_comparisons(results, results_folder)


def _collect_csn_negatives(count, pipeline):
    """Stream Python functions from CodeSearchNet and pair them across different repos.

    Cross-repo pairs are extremely unlikely to be semantic clones, giving clean
    out-of-domain negatives that break the PoolC same-distribution bias.
    """
    from datasets import load_dataset
    import random as _rng

    pipeline.status("Connecting to CodeSearchNet...")

    dataset = load_dataset(
        "code-search-net/code_search_net",
        "python",
        split="train",
        streaming=True,
    )

    # Collect ~2× target so we have slack to discard same-repo pairs
    target_funcs = count * 2 + 500
    funcs = []   # [(repo_name, func_code)]
    pipeline.status("Collecting functions from CodeSearchNet...")
    for row in dataset:
        code = (row.get("func_code_string") or "").strip()
        repo = row.get("repository_name") or ""
        if code and 30 <= len(code) <= 3000:
            funcs.append((repo, code))
        if len(funcs) >= target_funcs:
            break

    _rng.shuffle(funcs)

    # Split into two pools and pair functions from different repos
    mid    = len(funcs) // 2
    pool_a = funcs[:mid]
    pool_b = funcs[mid:]

    pairs = []
    j = 0
    for repo_a, code_a in pool_a:
        if len(pairs) >= count:
            break
        while j < len(pool_b):
            repo_b, code_b = pool_b[j]
            j += 1
            if repo_a != repo_b:
                pairs.append((code_a, code_b))
                pipeline.update("Collected")
                break

    logger.info("CSN negatives collected: %d requested, %d produced", count, len(pairs))
    return pairs


def _process_poolc(sample_size, pipeline, diverse_neg_ratio=0.0):
    from datasets import load_dataset, disable_progress_bar

    half         = sample_size // 2
    poolc_neg    = int(half * (1 - diverse_neg_ratio))
    csn_neg      = half - poolc_neg
    poolc_total  = half + poolc_neg   # positives + PoolC negatives

    # Suppress ALL HF/datasets output before the first pipeline draw.
    # These libraries write warnings and progress bars to stderr which interleave
    # with pipeline redraws and corrupt the line-count used for cursor positioning.
    disable_progress_bar()
    for _log in ("datasets", "huggingface_hub", "fsspec", "filelock"):
        logging.getLogger(_log).setLevel(logging.CRITICAL)

    _old_stderr, sys.stderr = sys.stderr, open(os.devnull, "w")
    try:
        pipeline.begin("Stream PoolC dataset", poolc_total, ["Streamed"])
        pipeline.status("Connecting to Hugging Face — this may take a moment...")

        dataset = load_dataset("PoolC/1-fold-clone-detection-600k-5fold", split="train", streaming=True)

        pipeline.status("Streaming pairs...")
        pairs_raw = []
        pos_count = neg_count = 0
        for row in dataset:
            if row["similar"] == 1 and pos_count < half:
                pairs_raw.append((row["code1"], row["code2"], 1))
                pos_count += 1
                pipeline.update("Streamed")
            elif row["similar"] == 0 and neg_count < poolc_neg:
                pairs_raw.append((row["code1"], row["code2"], 0))
                neg_count += 1
                pipeline.update("Streamed")
            if pos_count >= half and neg_count >= poolc_neg:
                break

        pipeline.finish()  # mark PoolC step as complete before starting CSN

        if csn_neg > 0:
            pipeline.begin("Stream CodeSearchNet", csn_neg, ["Collected"])
            csn_pairs = _collect_csn_negatives(csn_neg, pipeline)
            for code_a, code_b in csn_pairs:
                pairs_raw.append((code_a, code_b, 2))  # 2 = CSN negative sentinel
    finally:
        sys.stderr = _old_stderr

    # Reuse the last streaming step to show processing progress
    last_stream_step = "Stream CodeSearchNet" if csn_neg > 0 else "Stream PoolC dataset"
    pipeline.begin(last_stream_step, len(pairs_raw), ["Processed"])
    pipeline.status("Starting worker processes — may freeze briefly depending on hardware...")
    os.makedirs(TEMP_DIR, exist_ok=True)

    error_log = []
    labeled_pairs = []
    texts = {}
    feature_vecs = {}
    next_idx = [0]

    try:
        with ProcessPoolExecutor(initializer=_worker_init) as executor:
            pipeline.status(f"Queuing {len(pairs_raw)} pairs...")
            futures = {}
            for i, (code1, code2, label) in enumerate(pairs_raw):
                futures[executor.submit(_process_pair, code1, code2)] = (i, label)
                pipeline.ping()
            pipeline.status(f"Processing {len(pairs_raw)} pairs...")
            for future in as_completed(futures):
                i, label = futures[future]
                try:
                    feat_a, feat_b, text_a, text_b = future.result()
                    idx_a, idx_b = next_idx[0], next_idx[0] + 1
                    next_idx[0] += 2
                    texts[idx_a] = text_a
                    texts[idx_b] = text_b
                    feature_vecs[idx_a] = feat_a
                    feature_vecs[idx_b] = feat_b
                    labeled_pairs.append((idx_a, idx_b, label))
                    pipeline.update("Processed")
                except Exception as e:
                    logger.warning("pair %d failed: %s", i, e)
                    error_log.append(f"  pair {i}: {e}")
                    pipeline.update("Processed")
    except KeyboardInterrupt:
        pipeline.finish()
        pipeline.complete()
        print("\nInterrupted. Exiting.")
        shutil.rmtree(TEMP_DIR, ignore_errors=True)
        raise SystemExit

    pipeline.finish()

    positive_pairs       = [(a, b) for a, b, lbl in labeled_pairs if lbl == 1]
    poolc_negative_pairs = [(a, b) for a, b, lbl in labeled_pairs if lbl == 0]
    csn_negative_pairs   = [(a, b) for a, b, lbl in labeled_pairs if lbl == 2]
    error_count          = len(pairs_raw) - len(labeled_pairs)

    with open(TEXTS_CACHE_FILE, "wb") as f:
        pickle.dump(texts, f)
    np.savez(FEATURES_CACHE_FILE, **{str(k): v for k, v in feature_vecs.items()})

    return positive_pairs, poolc_negative_pairs, csn_negative_pairs, error_count, error_log


# ── Classifiers ───────────────────────────────────────────────────────────────

def _run_classifiers(positive_pairs, negative_pairs, poolc_negative_pairs,
                     results_folder, models_folder, opts: RunOptions, pipeline):
    from classifier import classify
    from baseline import baseline
    from jaccard_baseline import jaccard_baseline

    results = []

    if opts.run_goc:
        # GoCP uses all negatives (PoolC + CSN) to benefit from diverse training.
        r = classify(positive_pairs, negative_pairs, TEMP_DIR, results_folder,
                     models_folder, fixed_threshold=opts.fixed_threshold, pipeline=pipeline)
        results.append(r)

    if opts.run_tfidf:
        # TF-IDF uses PoolC-only negatives — CSN code shifts the vocabulary
        # distribution and breaks the feature space for competitive-programming eval.
        r = baseline(positive_pairs, poolc_negative_pairs, TEMP_DIR, results_folder,
                     keyword_only=False, models_folder=models_folder,
                     fixed_threshold=opts.fixed_threshold, pipeline=pipeline)
        results.append(r)

    if opts.run_tfidf_keywords:
        r = baseline(positive_pairs, poolc_negative_pairs, TEMP_DIR, results_folder,
                     keyword_only=True, models_folder=models_folder,
                     fixed_threshold=opts.fixed_threshold, pipeline=pipeline)
        results.append(r)

    if opts.run_jaccard:
        r = jaccard_baseline(positive_pairs, poolc_negative_pairs, TEMP_DIR, results_folder,
                             models_folder=models_folder, pipeline=pipeline)
        results.append(r)

    return results


def _run_comparisons(results, results_folder):
    by_name = {r["name"]: r for r in results}
    pairs = [
        ("GoCP",             "TF-IDF (Full)",      "statistical_comparison.csv"),
        ("GoCP",             "TF-IDF (Keywords)",  "statistical_comparison_keyword.csv"),
        ("GoCP",             "Jaccard",             "statistical_comparison_jaccard.csv"),
        ("TF-IDF (Full)",    "TF-IDF (Keywords)",  "statistical_comparison_tfidf_vs_keyword.csv"),
        ("TF-IDF (Full)",    "Jaccard",             "statistical_comparison_tfidf_vs_jaccard.csv"),
        ("TF-IDF (Keywords)","Jaccard",             "statistical_comparison_keyword_vs_jaccard.csv"),
    ]
    for name_a, name_b, filename in pairs:
        if name_a in by_name and name_b in by_name:
            ra, rb = by_name[name_a], by_name[name_b]
            print(f"\n{name_a} vs {name_b}:")
            _statistical_comparison(
                ra["fold_results"], rb["fold_results"],
                name_a, name_b, results_folder, filename,
            )


def _statistical_comparison(fold_results_a, fold_results_b, label_a, label_b, results_folder, filename):
    from scipy.stats import wilcoxon, norm

    f1_a = np.array([r[3] for r in fold_results_a])
    f1_b = np.array([r[3] for r in fold_results_b])

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
        logger.warning("Wilcoxon test failed (%s vs %s): %s", label_a, label_b, e)
        print(f"  Wilcoxon test failed: {e}")

    os.makedirs(results_folder, exist_ok=True)
    output_path = os.path.join(results_folder, filename)
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["fold", f"{label_a}_f1", f"{label_b}_f1", "difference"])
        for (fold, *_, fa), (_, *_, fb) in zip(fold_results_a, fold_results_b):
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


# ── Summary ───────────────────────────────────────────────────────────────────

def _print_summary(dataset_info, results, results_folder, models_folder):
    sep = "─" * 56
    print(sep)
    for line in dataset_info:
        print(line)
    if results:
        print()
        for r in results:
            name   = r["name"]
            thresh = r["threshold"]
            avg    = r["avg"]
            print(f"  {name:<22}  Threshold: {thresh:.2f}  |  "
                  f"P={avg['precision']:.4f}  R={avg['recall']:.4f}  F1={avg['f1']:.4f}")
    print()
    print(f"  Results saved to {results_folder}")
    if models_folder:
        print(f"  Models saved to  {models_folder}")
    print(sep)


# ── Processing helpers ─────────────────────────────────────────────────────────

def _process_file(filepath):
    from goc import goc
    from features import features
    from preprocess import preprocess
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
    from goc import goc
    from features import features
    from preprocess import preprocess
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
    max_attempts = count * 20
    while len(negative_pairs) < count and attempts < max_attempts:
        idx_a = random.randrange(0, total_funcs)
        idx_b = random.randrange(0, total_funcs)
        if idx_a != idx_b \
                and (idx_a // 2 != idx_b // 2) \
                and (min(idx_a, idx_b), max(idx_a, idx_b)) not in positive_set:
            negative_pairs.append((idx_a, idx_b))
        attempts += 1
    if len(negative_pairs) < count:
        logger.warning(
            "Could only generate %d negative pairs (wanted %d) after %d attempts — "
            "the function pool may be too small",
            len(negative_pairs), count, attempts,
        )
    return negative_pairs


if __name__ == "__main__":
    main()
