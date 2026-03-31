"""
Compute Accuracy, Precision, Recall, F1, and AUC-ROC for all four models
using 10-fold stratified cross-validation on the cached training data.
"""
import os, sys, json, pickle
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'train'))

import time
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, roc_auc_score)

TEMP_DIR = os.path.join(os.path.dirname(__file__), '..', 'temp')

# ── Load cached data ──────────────────────────────────────────────────────────

print("Loading cache...")
with open(os.path.join(TEMP_DIR, "pairs_cache.json")) as f:
    cache = json.load(f)

with open(os.path.join(TEMP_DIR, "texts_cache.pkl"), "rb") as f:
    texts = pickle.load(f)

feature_vecs = np.load(os.path.join(TEMP_DIR, "features_cache.npz"))

positive_pairs       = [tuple(p) for p in cache["positive_pairs"]]
poolc_negative_pairs = [tuple(p) for p in cache["poolc_negative_pairs"]]
csn_negative_pairs   = [tuple(p) for p in cache.get("csn_negative_pairs", [])]
all_negative_pairs   = poolc_negative_pairs + csn_negative_pairs

print(f"  Positive: {len(positive_pairs)}  Negative: {len(all_negative_pairs)}")

# ── Build pairwise feature matrices ──────────────────────────────────────────

def build_goc_features(pairs, labels):
    from utils import pairwise_goc_features
    X, y = [], []
    for (a, b), lbl in zip(pairs, labels):
        va = feature_vecs[str(a)]
        vb = feature_vecs[str(b)]
        X.append(pairwise_goc_features(va, vb))
        y.append(lbl)
    return np.array(X), np.array(y)


def build_tfidf_features(pairs, labels, keyword_only=False):
    from scipy import sparse
    from sklearn.feature_extraction.text import TfidfVectorizer

    _KW = (r"\b(?:False|None|True|and|as|assert|async|await|break|class|continue|"
           r"def|del|elif|else|except|finally|for|from|global|if|import|in|is|"
           r"lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)\b")
    token_pattern = _KW if keyword_only else r"[A-Za-z_]\w*|\S"

    all_idx = sorted({idx for a, b in pairs for idx in (a, b)})
    vectorizer = TfidfVectorizer(analyzer="word", token_pattern=token_pattern,
                                 max_features=2000)
    vectorizer.fit([texts[idx] for idx in all_idx])
    tfidf_matrix = vectorizer.transform([texts[idx] for idx in all_idx])
    idx_to_row = {idx: i for i, idx in enumerate(all_idx)}

    rows_a = [idx_to_row[a] for a, b in pairs]
    rows_b = [idx_to_row[b] for a, b in pairs]
    mat_a = tfidf_matrix[rows_a]
    mat_b = tfidf_matrix[rows_b]
    diff = mat_a - mat_b
    diff.data = np.abs(diff.data)
    X = sparse.hstack([mat_a, mat_b, diff], format="csr")
    return X, np.array(labels)


def build_jaccard_similarities(pairs, labels):
    from utils import jaccard_similarity
    print("  Computing Jaccard similarities (this may take a while)...")
    sims = np.array([jaccard_similarity(texts[a], texts[b]) for a, b in pairs])
    return sims, np.array(labels)


# ── Cross-validation ──────────────────────────────────────────────────────────

def run_cv(name, X, y, clf_factory):
    skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    metrics = {m: [] for m in ["accuracy", "precision", "recall", "f1", "auc_roc"]}

    for fold, (train_idx, test_idx) in enumerate(skf.split(X, y), 1):
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]

        clf = clf_factory()
        clf.fit(X_train, y_train)
        probs = clf.predict_proba(X_test)[:, 1]
        y_pred = (probs >= 0.5).astype(int)

        metrics["accuracy"].append(accuracy_score(y_test, y_pred))
        metrics["precision"].append(precision_score(y_test, y_pred, zero_division=0))
        metrics["recall"].append(recall_score(y_test, y_pred, zero_division=0))
        metrics["f1"].append(f1_score(y_test, y_pred, zero_division=0))
        metrics["auc_roc"].append(roc_auc_score(y_test, probs))

    print(f"\n{name}")
    print(f"  {'Metric':<12} {'Mean':>8}  {'Std':>8}")
    print(f"  {'-'*30}")
    for m, vals in metrics.items():
        print(f"  {m:<12} {np.mean(vals):>8.4f}  {np.std(vals):>8.4f}")
    return metrics


def run_cv_jaccard(name, sims, y):
    """Jaccard has no classifier — similarity score is used directly as probability."""
    skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    metrics = {m: [] for m in ["accuracy", "precision", "recall", "f1", "auc_roc"]}

    for fold, (train_idx, test_idx) in enumerate(skf.split(sims.reshape(-1, 1), y), 1):
        sim_train, y_train = sims[train_idx], y[train_idx]
        sim_test,  y_test  = sims[test_idx],  y[test_idx]

        # Find best threshold on train fold
        best_t, best_f1 = 0.5, -1.0
        for t in np.linspace(0.0, 1.0, 101):
            f1 = f1_score(y_train, (sim_train >= t).astype(int), zero_division=0)
            if f1 > best_f1:
                best_f1, best_t = f1, t

        y_pred = (sim_test >= best_t).astype(int)
        metrics["accuracy"].append(accuracy_score(y_test, y_pred))
        metrics["precision"].append(precision_score(y_test, y_pred, zero_division=0))
        metrics["recall"].append(recall_score(y_test, y_pred, zero_division=0))
        metrics["f1"].append(f1_score(y_test, y_pred, zero_division=0))
        metrics["auc_roc"].append(roc_auc_score(y_test, sim_test))

    print(f"\n{name}")
    print(f"  {'Metric':<12} {'Mean':>8}  {'Std':>8}")
    print(f"  {'-'*30}")
    for m, vals in metrics.items():
        print(f"  {m:<12} {np.mean(vals):>8.4f}  {np.std(vals):>8.4f}")
    return metrics


# ── Run all models ────────────────────────────────────────────────────────────

all_pairs  = positive_pairs + all_negative_pairs
all_labels = [1] * len(positive_pairs) + [0] * len(all_negative_pairs)

poolc_pairs  = positive_pairs + poolc_negative_pairs
poolc_labels = [1] * len(positive_pairs) + [0] * len(poolc_negative_pairs)

print("\nBuilding GoC features...")
X_goc, y_goc = build_goc_features(all_pairs, all_labels)

print("Building TF-IDF (Full) features...")
X_tfidf_full, y_tfidf_full = build_tfidf_features(poolc_pairs, poolc_labels, keyword_only=False)

print("Building TF-IDF (Keywords) features...")
X_tfidf_kw, y_tfidf_kw = build_tfidf_features(poolc_pairs, poolc_labels, keyword_only=True)

print("Building Jaccard similarities...")
sims_jac, y_jac = build_jaccard_similarities(poolc_pairs, poolc_labels)

print("\n" + "=" * 50)
print("10-Fold Cross-Validation Results")
print("=" * 50)

from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from scipy.stats import wilcoxon, norm
from itertools import combinations

all_results = {}

all_results["GoC (Graph-of-Code)"] = run_cv(
    "GoC (Graph-of-Code)", X_goc, y_goc,
    lambda: HistGradientBoostingClassifier(max_iter=500, early_stopping=True,
                                           random_state=42, class_weight="balanced"))

all_results["TF-IDF (Full)"] = run_cv(
    "TF-IDF (Full)", X_tfidf_full, y_tfidf_full,
    lambda: RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1))

all_results["TF-IDF (Keywords)"] = run_cv(
    "TF-IDF (Keywords)", X_tfidf_kw, y_tfidf_kw,
    lambda: RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1))

all_results["Jaccard Similarity"] = run_cv_jaccard(
    "Jaccard Similarity", sims_jac, y_jac)

# ── Wilcoxon pairwise tests ───────────────────────────────────────────────────

print("\n" + "=" * 60)
print("Pairwise Wilcoxon Signed-Rank Tests")
print("=" * 60)

model_names = list(all_results.keys())
metrics_to_test = ["accuracy", "f1", "auc_roc"]

for metric in metrics_to_test:
    print(f"\n-- {metric.upper()} --")
    print(f"  {'Comparison':<45} {'W':>8}  {'p':>8}  {'r':>6}  Sig  Winner")
    print(f"  {'-'*85}")
    for name_a, name_b in combinations(model_names, 2):
        vals_a = np.array(all_results[name_a][metric])
        vals_b = np.array(all_results[name_b][metric])
        mean_a, mean_b = np.mean(vals_a), np.mean(vals_b)
        try:
            stat, p = wilcoxon(vals_a, vals_b, alternative="two-sided")
            z = abs(norm.ppf(p / 2))
            r = z / np.sqrt(len(vals_a))
            sig = "*" if p < 0.05 else " "
            winner = name_a if mean_a > mean_b else name_b
            winner_str = winner if p < 0.05 else "-"
            label = f"{name_a} vs {name_b}"
            print(f"  {label:<45} {stat:>8.2f}  {p:>8.4f}  {r:>6.4f}  {sig}    {winner_str}")
        except Exception as e:
            print(f"  {name_a} vs {name_b}: could not compute ({e})")

# ── End-to-end timing ─────────────────────────────────────────────────────────
# Times the full pipeline: raw source → preprocessing → feature extraction → prediction.

print("\n" + "=" * 50)
print("End-to-End Prediction Time (per pair, ms)")
print("=" * 50)

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))
from predictor import predict_goc, predict_tfidf, predict_jaccard

N_SAMPLES = 100
rng = np.random.default_rng(42)
sample_idx = rng.choice(len(all_pairs), size=N_SAMPLES, replace=False)
sample_pairs = [all_pairs[i] for i in sample_idx]

e2e_models = {
    "GoC (Graph-of-Code)":   lambda a, b: predict_goc(a, b),
    "TF-IDF (Full)":         lambda a, b: predict_tfidf(a, b, keyword_only=False),
    "TF-IDF (Keywords)":     lambda a, b: predict_tfidf(a, b, keyword_only=True),
    "Jaccard Similarity":    lambda a, b: predict_jaccard(a, b),
}

print(f"  Benchmarking on {N_SAMPLES} pairs...")
print(f"  {'Model':<25} {'Mean (ms)':>10}  {'Std (ms)':>10}")
print(f"  {'-'*48}")

for model_name, predict_fn in e2e_models.items():
    times_ms = []
    for a_idx, b_idx in sample_pairs:
        text_a = texts[a_idx]
        text_b = texts[b_idx]
        t0 = time.perf_counter()
        predict_fn(text_a, text_b)
        times_ms.append((time.perf_counter() - t0) * 1000)
    print(f"  {model_name:<25} {np.mean(times_ms):>10.2f}  {np.std(times_ms):>10.2f}")
