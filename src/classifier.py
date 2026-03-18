import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import canberra, cosine
from scipy.stats import pearsonr
import csv
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


def classify(positive_pairs, negative_pairs, temp_dir, results_folder):
    # Build dataset: 168 structural features + 4 similarity metrics = 172 features

    # Load all feature vectors — use single cache file if available
    features_cache_path = os.path.join(temp_dir, "features_cache.npz")
    if os.path.exists(features_cache_path):
        print("  Loading features cache...")
        cache = np.load(features_cache_path)
        def load_vec(idx):
            return np.nan_to_num(cache[str(idx)], nan=0.0, posinf=0.0, neginf=0.0)
    else:
        def load_vec(idx):
            v = np.load(os.path.join(temp_dir, f"func_{idx}.npy"))
            return np.nan_to_num(v, nan=0.0, posinf=0.0, neginf=0.0)

    X = []
    y = []

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

    # Scale features so large-magnitude features don't dominate |A-B|
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # 10-fold stratified cross-validation
    skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    clf = RandomForestClassifier(n_estimators=300, random_state=42, n_jobs=-1)

    fold_results = []
    progress = ProgressBar(10, ["Folds"])
    progress.status("Starting cross-validation...")

    for fold, (train_idx, test_idx) in enumerate(skf.split(X, y), start=1):
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]

        progress.status(f"Fold {fold}/10: Training...")
        clf.fit(X_train, y_train)

        progress.status(f"Fold {fold}/10: Evaluating...")
        y_pred = clf.predict(X_test)

        precision = precision_score(y_test, y_pred, zero_division=0)
        recall = recall_score(y_test, y_pred, zero_division=0)
        f1 = f1_score(y_test, y_pred, zero_division=0)

        fold_results.append((fold, precision, recall, f1))
        progress.update("Folds")

    progress.finish()

    avg_precision = np.mean([r[1] for r in fold_results])
    avg_recall = np.mean([r[2] for r in fold_results])
    avg_f1 = np.mean([r[3] for r in fold_results])

    print(f"  {'Average':8s}: Precision={avg_precision:.4f}  Recall={avg_recall:.4f}  F1={avg_f1:.4f}")

    # Save results to CSV
    os.makedirs(results_folder, exist_ok=True)
    output_path = os.path.join(results_folder, "gocp_results.csv")

    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["fold", "precision", "recall", "f1"])
        for row in fold_results:
            writer.writerow(row)
        writer.writerow(["average", avg_precision, avg_recall, avg_f1])

    print(f"Results saved to {output_path}")
