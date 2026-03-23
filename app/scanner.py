"""Extract and preprocess Python functions from source code."""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import ast
import textwrap
from preprocess import preprocess


def extract_functions(source: str) -> list[tuple[str, str]]:
    """
    Return a list of (name, source_text) for each top-level function in source.
    Falls back to returning the whole source as a single unnamed function if
    parsing fails or no functions are found.
    """
    source = textwrap.dedent(preprocess(source))
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return [("<snippet>", source.strip())]

    functions = []
    lines = source.splitlines(keepends=True)

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            # Only keep top-level functions (parent is Module)
            start = node.lineno - 1
            end = node.end_lineno
            func_source = "".join(lines[start:end]).rstrip()
            functions.append((node.name, func_source))

    if not functions:
        return [("<snippet>", source.strip())]

    # Deduplicate: keep only first occurrence of each name
    seen = set()
    unique = []
    for name, src in functions:
        if name not in seen:
            seen.add(name)
            unique.append((name, src))

    return unique


def get_function_features(source: str):
    """
    Preprocess source and compute GoC feature vector.
    Returns (preprocessed_text, feature_vector).
    """
    from goc import goc
    from features import features

    preprocessed = textwrap.dedent(preprocess(source))
    vec = features(goc(preprocessed))
    return preprocessed, vec
