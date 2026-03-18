import argparse
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

_FUNC_DEF_PATTERN = re.compile(r"^(def\s+(\w+)\s*\()", re.MULTILINE)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default=DEFAULT_DATA_FOLDER,
                        help=f"Path to the data folder (default: {DEFAULT_DATA_FOLDER})")
    parser.add_argument("--results", default=DEFAULT_RESULTS_FOLDER,
                        help=f"Path to the results folder (default: {DEFAULT_RESULTS_FOLDER})")
    parser.add_argument("--show-errors", action="store_true",
                        help="Display error details for each failed file")
    parser.add_argument("--baseline", action="store_true",
                        help="Run TF-IDF baseline classifier for comparison")
    args = parser.parse_args()

    print(f"Starting model training for dataset")
    print(f"----------")
    print(f"Data folder: {args.data}")
    print(f"Results folder: {args.results}")
    print(f"----------")
    print(f"Processing data files")
    load_data(args.data, args.results, show_errors=args.show_errors, run_baseline=args.baseline)


def load_data(data_folder, results_folder, show_errors=False, run_baseline=False):
    py_files = [
        os.path.join(root, f)
        for root, _, files in os.walk(data_folder)
        for f in files if f.endswith(".py")
    ]

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
                        features_a, features_b, text_a, text_b = result
                        idx_a, idx_b = _save_pair(features_a, features_b, text_a, text_b, func_index)
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

    print("Running GoC classifier...")
    classify(positive_pairs, negative_pairs, TEMP_DIR, results_folder)
    if run_baseline:
        from baseline import baseline
        print("Running TF-IDF baseline...")
        baseline(positive_pairs, negative_pairs, TEMP_DIR, results_folder)

    shutil.rmtree(TEMP_DIR, ignore_errors=True)


def _process_file(filepath):
    """Load, preprocess, find clone pair, and compute features.
    Returns (features_a, features_b) or None if no clone pair found.
    Runs in a worker process.
    """
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


def _extract_function(source, start_pos, all_matches):
    for match in all_matches:
        if match.start() > start_pos:
            return source[start_pos:match.start()].rstrip()
    return source[start_pos:].rstrip()


def _save_pair(features_a, features_b, text_a, text_b, func_index):
    idx_a, idx_b = func_index[0], func_index[0] + 1
    func_index[0] += 2
    np.save(os.path.join(TEMP_DIR, f"func_{idx_a}.npy"), features_a)
    np.save(os.path.join(TEMP_DIR, f"func_{idx_b}.npy"), features_b)
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
