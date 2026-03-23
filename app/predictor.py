"""Load saved models and predict clone probability for a pair of functions."""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import re
import numpy as np

MODELS_DIR = os.path.join(os.path.dirname(__file__), '..', 'models')

_PYTHON_KEYWORDS_PATTERN = (
    r"\b(?:False|None|True|and|as|assert|async|await|break|class|continue|"
    r"def|del|elif|else|except|finally|for|from|global|if|import|in|is|"
    r"lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)\b"
)


def _load_model(filename):
    import joblib
    path = os.path.join(MODELS_DIR, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Model file not found: {path}\n"
            f"Train it first with: python train/main.py --save-models --poolc"
        )
    return joblib.load(path)


def predict_goc(text_a: str, text_b: str) -> tuple[int, float]:
    """Predict using the GoC + RandomForest model."""
    from scanner import get_function_features
    from scipy.spatial.distance import canberra, cosine
    from scipy.stats import pearsonr

    model = _load_model("goc_model.joblib")
    scaler = model["scaler"]
    clf = model["clf"]

    _, vec_a = get_function_features(text_a)
    _, vec_b = get_function_features(text_b)

    vec_a = np.nan_to_num(vec_a, nan=0.0, posinf=0.0, neginf=0.0)
    vec_b = np.nan_to_num(vec_b, nan=0.0, posinf=0.0, neginf=0.0)

    try:
        canberra_dist = canberra(vec_a, vec_b)
    except Exception:
        canberra_dist = 0.0
    try:
        cosine_dist = cosine(vec_a, vec_b)
    except Exception:
        cosine_dist = 0.0
    euclidean_dist = float(np.linalg.norm(vec_a - vec_b))
    try:
        corr, _ = pearsonr(vec_a, vec_b)
        corr = 0.0 if np.isnan(corr) else corr
    except Exception:
        corr = 0.0
    sim = np.array([canberra_dist, cosine_dist, euclidean_dist, corr])

    X = np.concatenate([vec_a, vec_b, np.abs(vec_a - vec_b), sim]).reshape(1, -1)
    X = scaler.transform(X)

    prob = float(clf.predict_proba(X)[0][1])
    threshold = model.get("threshold", 0.5)
    label = int(prob >= threshold)
    return label, prob


def predict_tfidf(text_a: str, text_b: str, keyword_only: bool = False) -> tuple[int, float]:
    """Predict using TF-IDF + RandomForest model."""
    from scipy import sparse

    filename = "tfidf_keyword_model.joblib" if keyword_only else "tfidf_full_model.joblib"
    model = _load_model(filename)
    vectorizer = model["vectorizer"]
    clf = model["clf"]

    vec_a = vectorizer.transform([text_a])
    vec_b = vectorizer.transform([text_b])
    diff = vec_a - vec_b
    diff.data = np.abs(diff.data)
    X = sparse.hstack([vec_a, vec_b, diff], format="csr")

    prob = float(clf.predict_proba(X)[0][1])
    threshold = model.get("threshold", 0.5)
    label = int(prob >= threshold)
    return label, prob


def predict_jaccard(text_a: str, text_b: str) -> tuple[int, float]:
    """Predict using Jaccard similarity threshold."""
    model = _load_model("jaccard_model.joblib")
    threshold = model["threshold"]

    tokens_a = set(text_a.split())
    tokens_b = set(text_b.split())
    if not tokens_a and not tokens_b:
        similarity = 1.0
    elif not tokens_a or not tokens_b:
        similarity = 0.0
    else:
        similarity = len(tokens_a & tokens_b) / len(tokens_a | tokens_b)

    label = int(similarity >= threshold)
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
        raise ValueError(f"Unknown method: {method}")
    return METHODS[method](text_a, text_b)
