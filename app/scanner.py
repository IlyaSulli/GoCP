"""Extract and preprocess Python functions from source code."""
import ast
import logging
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import textwrap
from preprocess import preprocess

logger = logging.getLogger(__name__)


def extract_functions(source: str) -> list[tuple[str, str]]:
    """
    Return a list of (name, source_text) for each top-level function in source.
    Falls back to returning the whole source as a single unnamed function if
    parsing fails or no functions are found.
    """
    source = textwrap.dedent(preprocess(source))
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        logger.warning("SyntaxError parsing source; falling back to raw snippet: %s", exc)
        return [("<snippet>", source.strip())]

    functions = []
    lines = source.splitlines(keepends=True)

    # Only collect direct children of the Module node (top-level functions).
    # ast.walk would also yield nested functions inside classes or other
    # functions, which we do not want here.
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            start = node.lineno - 1
            end   = node.end_lineno
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

    if not source or not source.strip():
        raise ValueError("Source code is empty.")

    preprocessed = textwrap.dedent(preprocess(source))
    vec = features(goc(preprocessed))
    return preprocessed, vec
