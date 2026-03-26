"""Shared utilities used by both training and inference."""
import logging

import numpy as np
from scipy.spatial.distance import canberra, cosine
from scipy.stats import pearsonr

logger = logging.getLogger(__name__)


def similarity_features(vec_a: np.ndarray, vec_b: np.ndarray) -> np.ndarray:
    """
    Return [canberra, cosine, euclidean, pearson_r] for a pair of feature vectors.
    Each metric falls back to 0.0 if the inputs are degenerate (e.g. zero vectors).
    """
    try:
        canberra_dist = float(canberra(vec_a, vec_b))
    except Exception as exc:
        logger.warning("canberra distance failed: %s", exc)
        canberra_dist = 0.0

    try:
        cosine_dist = float(cosine(vec_a, vec_b))
    except Exception as exc:
        logger.warning("cosine distance failed: %s", exc)
        cosine_dist = 0.0

    euclidean_dist = float(np.linalg.norm(vec_a - vec_b))

    try:
        corr, _ = pearsonr(vec_a, vec_b)
        corr = 0.0 if not np.isfinite(corr) else float(corr)
    except Exception as exc:
        logger.warning("pearsonr failed: %s", exc)
        corr = 0.0

    return np.array([canberra_dist, cosine_dist, euclidean_dist, corr])


def jaccard_similarity(text_a: str, text_b: str) -> float:
    """
    Token-level Jaccard similarity between two code strings (whitespace-tokenised).
    Returns 1.0 if both are empty, 0.0 if only one is empty.
    """
    tokens_a = set(text_a.split())
    tokens_b = set(text_b.split())
    if not tokens_a and not tokens_b:
        return 1.0
    if not tokens_a or not tokens_b:
        return 0.0
    return len(tokens_a & tokens_b) / len(tokens_a | tokens_b)
