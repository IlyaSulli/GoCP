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


def pairwise_goc_features(vec_a: np.ndarray, vec_b: np.ndarray) -> np.ndarray:
    """
    Compute pairwise comparison features between two GoC fingerprint vectors.

    Uses only relative/comparative measures so the classifier cannot learn
    domain shortcuts (e.g. "both vectors look like competitive-programming
    code → clone").  The output is entirely domain-agnostic.

    Input: 56-dimensional GoC fingerprints [0:48 node stats, 48:56 graph props].

    Output (4×56 + 1 + 4 = 229 features):
      56  absolute element-wise difference  |va - vb|
      56  element-wise Canberra components  |va-vb|/(|va|+|vb|+ε)  [paper metric, Fig.5]
      56  element-wise proportionality      min/max ratio, 0.0 when both absent
      56  both-nonzero indicator            1.0 when both functions have this feature
       1  size ratio                        min(n_a,n_b)/(max(n_a,n_b)+1)
       4  global similarity metrics         [canberra, cosine, euclidean, pearson]
    Total: 229 features
    """
    abs_a = np.abs(vec_a)
    abs_b = np.abs(vec_b)
    abs_diff = np.abs(vec_a - vec_b)

    # Element-wise Canberra (the paper's core metric, scale-invariant).
    canberra_elems = abs_diff / (abs_a + abs_b + 1e-10)

    # Element-wise proportionality ratio.
    # safe_max avoids divide-by-zero warnings from numpy evaluating both
    # np.where branches before applying the mask.
    elem_max = np.maximum(abs_a, abs_b)
    elem_min = np.minimum(abs_a, abs_b)
    safe_max = np.where(elem_max > 1e-10, elem_max, 1.0)
    # 0.0 when both absent: coincidental zeros are not evidence of similarity.
    min_ratio = np.where(elem_max > 1e-10, elem_min / safe_max, 0.0)

    # Reliability indicator: Canberra/ratio are only meaningful when both present.
    both_nonzero = ((abs_a > 1e-10) & (abs_b > 1e-10)).astype(float)

    # Explicit size ratio (network_size is at feature index 48).
    n_a = max(float(vec_a[48]), 1.0)
    n_b = max(float(vec_b[48]), 1.0)
    size_ratio = np.array([min(n_a, n_b) / (max(n_a, n_b) + 1.0)])

    global_sim = similarity_features(vec_a, vec_b)

    return np.concatenate([abs_diff, canberra_elems, min_ratio, both_nonzero,
                           size_ratio, global_sim])


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
