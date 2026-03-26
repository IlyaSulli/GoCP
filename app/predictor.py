"""Load saved models and predict clone probability for a pair of functions."""
import logging
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import numpy as np
from utils import similarity_features, jaccard_similarity

logger = logging.getLogger(__name__)

MODELS_DIR = os.path.join(os.path.dirname(__file__), '..', 'models')


def _load_model(filename: str) -> dict:
    import joblib
    path = os.path.join(MODELS_DIR, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Model file not found: {path}\n"
            f"Train it first with: python train/main.py --save-models --poolc"
        )
    return joblib.load(path)


def _get_threshold(model: dict, filename: str) -> float:
    if "threshold" not in model:
        logger.warning("Model %s has no saved threshold; defaulting to 0.5", filename)
        return 0.5
    return float(model["threshold"])


def _validate_inputs(text_a: str, text_b: str) -> None:
    if not text_a or not text_a.strip():
        raise ValueError("Function A is empty.")
    if not text_b or not text_b.strip():
        raise ValueError("Function B is empty.")


def predict_goc(text_a: str, text_b: str) -> tuple[int, float]:
    """Predict using the GoC + RandomForest model."""
    from scanner import get_function_features

    _validate_inputs(text_a, text_b)

    model = _load_model("goc_model.joblib")
    scaler = model["scaler"]
    clf    = model["clf"]
    threshold = _get_threshold(model, "goc_model.joblib")

    _, vec_a = get_function_features(text_a)
    _, vec_b = get_function_features(text_b)

    vec_a = np.nan_to_num(vec_a, nan=0.0, posinf=0.0, neginf=0.0)
    vec_b = np.nan_to_num(vec_b, nan=0.0, posinf=0.0, neginf=0.0)

    sim = similarity_features(vec_a, vec_b)
    X = np.concatenate([vec_a, vec_b, np.abs(vec_a - vec_b), sim]).reshape(1, -1)
    X = scaler.transform(X)

    prob = float(clf.predict_proba(X)[0][1])
    label = int(prob >= threshold)
    logger.info("predict_goc: prob=%.4f threshold=%.2f label=%d", prob, threshold, label)
    return label, prob


def predict_tfidf(text_a: str, text_b: str, keyword_only: bool = False) -> tuple[int, float]:
    """Predict using TF-IDF + RandomForest model."""
    from scipy import sparse

    _validate_inputs(text_a, text_b)

    filename = "tfidf_keyword_model.joblib" if keyword_only else "tfidf_full_model.joblib"
    model = _load_model(filename)
    vectorizer = model["vectorizer"]
    clf        = model["clf"]
    threshold  = _get_threshold(model, filename)

    vec_a = vectorizer.transform([text_a])
    vec_b = vectorizer.transform([text_b])
    diff = vec_a - vec_b
    diff.data = np.abs(diff.data)
    X = sparse.hstack([vec_a, vec_b, diff], format="csr")

    prob = float(clf.predict_proba(X)[0][1])
    label = int(prob >= threshold)
    logger.info("predict_tfidf(keyword_only=%s): prob=%.4f threshold=%.2f label=%d",
                keyword_only, prob, threshold, label)
    return label, prob


def predict_jaccard(text_a: str, text_b: str) -> tuple[int, float]:
    """Predict using Jaccard similarity threshold."""
    _validate_inputs(text_a, text_b)

    model = _load_model("jaccard_model.joblib")
    threshold = _get_threshold(model, "jaccard_model.joblib")

    similarity = jaccard_similarity(text_a, text_b)
    label = int(similarity >= threshold)
    logger.info("predict_jaccard: similarity=%.4f threshold=%.2f label=%d",
                similarity, threshold, label)
    return label, similarity


METHODS = {
    "GoC (Graph-of-Code)":       lambda a, b: predict_goc(a, b),
    "TF-IDF (full)":             lambda a, b: predict_tfidf(a, b, keyword_only=False),
    "TF-IDF (keywords only)":    lambda a, b: predict_tfidf(a, b, keyword_only=True),
    "Jaccard similarity":         lambda a, b: predict_jaccard(a, b),
}


def available_methods() -> list[str]:
    """Return names of methods whose model files exist."""
    filenames = {
        "GoC (Graph-of-Code)":    "goc_model.joblib",
        "TF-IDF (full)":          "tfidf_full_model.joblib",
        "TF-IDF (keywords only)": "tfidf_keyword_model.joblib",
        "Jaccard similarity":      "jaccard_model.joblib",
    }
    return [name for name, fn in filenames.items()
            if os.path.exists(os.path.join(MODELS_DIR, fn))]


def predict(method: str, text_a: str, text_b: str) -> tuple[int, float]:
    """Run the chosen method. Returns (label, score) where score is probability or similarity."""
    if method not in METHODS:
        raise ValueError(f"Unknown method: {method!r}")
    return METHODS[method](text_a, text_b)
