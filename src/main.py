import argparse
import os
import re

from goc import goc

DEFAULT_DATA_FOLDER = "./data/"
DEFAULT_RESULTS_FOLDER = "./results/"


def main():
    # Get Arguments for data and results folder location
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default=DEFAULT_DATA_FOLDER,
                        help=f"Path to the data folder (default: {DEFAULT_DATA_FOLDER})")
    parser.add_argument("--results", default=DEFAULT_RESULTS_FOLDER,
                        help=f"Path to the results folder (default: {DEFAULT_RESULTS_FOLDER})")
    args = parser.parse_args()

    data_folder = args.data
    results_folder = args.results

    print(f"Starting model training for dataset")
    print(f"----------")
    print(f"Data folder: {data_folder}")
    print(f"Results folder: {results_folder}")
    print(f"----------")
    print(f"Loading data files")
    load_data(data_folder, results_folder)


def load_data(data_folder, results_folder):
    # Pattern to match function definitions at any indentation level
    func_def_pattern = re.compile(r"^(def\s+(\w+)\s*\()", re.MULTILINE)

    for root, _, files in os.walk(data_folder):
        for filename in files:
            if not filename.endswith(".py"):
                continue

            filepath = os.path.join(root, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    source = f.read()

                # Find all function definitions and their positions
                matches = list(func_def_pattern.finditer(source))

                # Group by function name
                functions_by_name = {}
                for match in matches:
                    name = match.group(2)
                    if name not in functions_by_name:
                        functions_by_name[name] = []
                    functions_by_name[name].append(match.start())

                # Find a function name that appears exactly twice (the clone pair)
                clone_pair_found = False
                for func_name, positions in functions_by_name.items():
                    if len(positions) == 2:
                        clone_a = extract_function(source, positions[0], matches)
                        clone_b = extract_function(source, positions[1], matches)

                        print(f"  [LOADED] {filepath}")
                        goc(clone_a, clone_b, results_folder)
                        clone_pair_found = True
                        break

                if not clone_pair_found:
                    print(f"  [SKIPPED] {filepath}: No clone pair found")

            except Exception as e:
                print(f"  [ERROR] {filepath}: {e}")


def extract_function(source, start_pos, all_matches):
    """Extract a function's source from start_pos until the next top-level def or EOF."""
    # Find the next function definition after this one
    for match in all_matches:
        if match.start() > start_pos:
            return source[start_pos:match.start()].rstrip()

    # No next function — take everything to end of file
    return source[start_pos:].rstrip()


if __name__ == "__main__":
    main()
