import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import csv
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.pipeline import Pipeline as SKPipeline
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import canberra, cosine
from scipy.stats import pearsonr
from progress import ProgressBar


def _similarity_features(vec_a, vec_b):
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
    return np.array([canberra_dist, cosine_dist, euclidean_dist, corr])


def classify(positive_pairs, negative_pairs, temp_dir, results_folder, models_folder=None, fixed_threshold=False, pipeline=None):
    features_cache_path = os.path.join(temp_dir, "features_cache.npz")
    if os.path.exists(features_cache_path):
        cache = np.load(features_cache_path)
        def load_vec(idx):
            return np.nan_to_num(cache[str(idx)], nan=0.0, posinf=0.0, neginf=0.0)
    else:
        def load_vec(idx):
            v = np.load(os.path.join(temp_dir, f"func_{idx}.npy"))
            return np.nan_to_num(v, nan=0.0, posinf=0.0, neginf=0.0)

    X, y = [], []
    for idx_a, idx_b in positive_pairs:
        vec_a, vec_b = load_vec(idx_a), load_vec(idx_b)
        sim = _similarity_features(vec_a, vec_b)
        X.append(np.concatenate([vec_a, vec_b, np.abs(vec_a - vec_b), sim]))
        y.append(1)
    for idx_a, idx_b in negative_pairs:
        vec_a, vec_b = load_vec(idx_a), load_vec(idx_b)
        sim = _similarity_features(vec_a, vec_b)
        X.append(np.concatenate([vec_a, vec_b, np.abs(vec_a - vec_b), sim]))
        y.append(0)

    X = np.array(X)
    y = np.array(y)

    # Hold out 15% as a validation set for threshold tuning
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.15, random_state=42, stratify=y
    )

    # Pipeline ensures the scaler is fit only on the CV training fold in each split,
    # preventing leakage from the test fold's statistics into the scaler.
    pipe = SKPipeline([
        ("scaler", StandardScaler()),
        ("clf", RandomForestClassifier(n_estimators=300, random_state=42, n_jobs=-1)),
    ])

    skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    total_steps = 10 + (2 if models_folder else 1)  # folds + threshold + optional save

    if pipeline is not None:
        pipeline.begin("Train GoCP", total_steps, ["Folds"])
        progress = pipeline
    else:
        progress = ProgressBar(total_steps, ["Folds"])

    # Find threshold on held-out validation set before CV so fold metrics match deployment
    if fixed_threshold:
        best_threshold = 0.5
        progress.status("Using fixed threshold: 0.50")
    else:
        progress.status("Finding optimal threshold on validation set...")
        pipe.fit(X_train, y_train)
        val_probs = pipe.predict_proba(X_val)[:, 1]
        best_threshold, best_val_f1 = 0.5, -1.0
        for t in np.linspace(0.0, 1.0, 101):
            f1 = f1_score(y_val, (val_probs >= t).astype(int), zero_division=0)
            if f1 > best_val_f1:
                best_val_f1, best_threshold = f1, t
        progress.status(f"Threshold: {best_threshold:.2f}  (val F1={best_val_f1:.4f})")
    progress.update("Folds")

    fold_results = []
    for fold, (train_idx, test_idx) in enumerate(skf.split(X_train, y_train), start=1):
        progress.status(f"Fold {fold}/10: Training...")
        pipe.fit(X_train[train_idx], y_train[train_idx])
        progress.status(f"Fold {fold}/10: Evaluating...")
        probs = pipe.predict_proba(X_train[test_idx])[:, 1]
        y_pred = (probs >= best_threshold).astype(int)
        precision = precision_score(y_train[test_idx], y_pred, zero_division=0)
        recall    = recall_score(y_train[test_idx], y_pred, zero_division=0)
        f1        = f1_score(y_train[test_idx], y_pred, zero_division=0)
        fold_results.append((fold, precision, recall, f1))
        progress.update("Folds")

    avg_precision = np.mean([r[1] for r in fold_results])
    avg_recall    = np.mean([r[2] for r in fold_results])
    avg_f1        = np.mean([r[3] for r in fold_results])

    model_path = None
    if models_folder:
        import joblib
        os.makedirs(models_folder, exist_ok=True)
        progress.status("Saving GoCP model...")
        pipe.fit(X_train, y_train)
        model_path = os.path.join(models_folder, "goc_model.joblib")
        joblib.dump({
            "scaler": pipe.named_steps["scaler"],
            "clf": pipe.named_steps["clf"],
            "threshold": best_threshold,
        }, model_path)
        progress.update("Folds")

    progress.finish()

    os.makedirs(results_folder, exist_ok=True)
    output_path = os.path.join(results_folder, "gocp_results.csv")
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["fold", "precision", "recall", "f1"])
        for row in fold_results:
            writer.writerow(row)
        writer.writerow(["average", avg_precision, avg_recall, avg_f1])

    return {
        "name": "GoCP",
        "fold_results": fold_results,
        "threshold": best_threshold,
        "avg": {"precision": avg_precision, "recall": avg_recall, "f1": avg_f1},
        "path": output_path,
    }
