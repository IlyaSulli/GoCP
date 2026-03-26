import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import csv
import pickle
import numpy as np
from scipy import sparse
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.feature_extraction.text import TfidfVectorizer
from progress import ProgressBar


_PYTHON_KEYWORDS_PATTERN = (
    r"\b(?:False|None|True|and|as|assert|async|await|break|class|continue|"
    r"def|del|elif|else|except|finally|for|from|global|if|import|in|is|"
    r"lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)\b"
)


def baseline(positive_pairs, negative_pairs, temp_dir, results_folder, keyword_only=False, models_folder=None, fixed_threshold=False, pipeline=None):
    all_indices = set()
    for idx_a, idx_b in positive_pairs + negative_pairs:
        all_indices.add(idx_a)
        all_indices.add(idx_b)

    texts_cache_path = os.path.join(temp_dir, "texts_cache.pkl")
    if os.path.exists(texts_cache_path):
        with open(texts_cache_path, "rb") as f:
            texts = pickle.load(f)
    else:
        texts = {}
        for idx in all_indices:
            with open(os.path.join(temp_dir, f"func_{idx}.txt"), "r", encoding="utf-8") as f:
                texts[idx] = f.read()

    step_name    = "Train TF-IDF (Keywords)" if keyword_only else "Train TF-IDF (Full)"
    token_pattern = _PYTHON_KEYWORDS_PATTERN if keyword_only else r"[A-Za-z_]\w*|\S"

    total_steps = 10 + (3 if models_folder else 2)  # matrix build + threshold + folds + optional save

    if pipeline is not None:
        pipeline.begin(step_name, total_steps, ["Folds"])
        progress = pipeline
    else:
        progress = ProgressBar(total_steps, ["Folds"])

    progress.status(f"Fitting {step_name} vectorizer...")
    all_idx_list = sorted(all_indices)
    vectorizer = TfidfVectorizer(analyzer="word", token_pattern=token_pattern, max_features=2000)
    vectorizer.fit([texts[idx] for idx in all_idx_list])

    progress.status("Building feature matrix...")
    tfidf_matrix = vectorizer.transform([texts[idx] for idx in all_idx_list])
    idx_to_row = {idx: i for i, idx in enumerate(all_idx_list)}

    all_pairs = positive_pairs + negative_pairs
    rows_a = [idx_to_row[a] for a, b in all_pairs]
    rows_b = [idx_to_row[b] for a, b in all_pairs]

    mat_a = tfidf_matrix[rows_a]
    mat_b = tfidf_matrix[rows_b]
    diff = mat_a - mat_b
    diff.data = np.abs(diff.data)
    X = sparse.hstack([mat_a, mat_b, diff], format="csr")
    y = np.array([1] * len(positive_pairs) + [0] * len(negative_pairs))
    progress.update("Folds")

    # Hold out 15% as a validation set for threshold tuning
    all_indices_split = np.arange(X.shape[0])
    train_idx_split, val_idx_split = train_test_split(
        all_indices_split, test_size=0.15, random_state=42, stratify=y
    )
    X_train, X_val = X[train_idx_split], X[val_idx_split]
    y_train, y_val = y[train_idx_split], y[val_idx_split]

    clf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    clf.fit(X_train, y_train)

    if fixed_threshold:
        best_threshold = 0.5
        progress.status("Using fixed threshold: 0.50")
    else:
        progress.status("Finding optimal threshold on validation set...")
        val_probs = clf.predict_proba(X_val)[:, 1]
        best_threshold, best_val_f1 = 0.5, -1.0
        for t in np.linspace(0.0, 1.0, 101):
            f1 = f1_score(y_val, (val_probs >= t).astype(int), zero_division=0)
            if f1 > best_val_f1:
                best_val_f1, best_threshold = f1, t
        progress.status(f"Threshold: {best_threshold:.2f}  (val F1={best_val_f1:.4f})")
    progress.update("Folds")

    skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    fold_results = []

    for fold, (train_idx, test_idx) in enumerate(skf.split(X_train, y_train), start=1):
        progress.status(f"Fold {fold}/10: Training...")
        clf.fit(X_train[train_idx], y_train[train_idx])
        progress.status(f"Fold {fold}/10: Evaluating...")
        probs = clf.predict_proba(X_train[test_idx])[:, 1]
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
        model_name = "tfidf_keyword_model.joblib" if keyword_only else "tfidf_full_model.joblib"
        progress.status(f"Saving {step_name} model...")
        clf.fit(X_train, y_train)
        model_path = os.path.join(models_folder, model_name)
        joblib.dump({"vectorizer": vectorizer, "clf": clf, "keyword_only": keyword_only, "threshold": best_threshold}, model_path)
        progress.update("Folds")

    progress.finish()

    os.makedirs(results_folder, exist_ok=True)
    filename = "keyword_baseline_results.csv" if keyword_only else "baseline_results.csv"
    output_path = os.path.join(results_folder, filename)
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["fold", "precision", "recall", "f1"])
        for row in fold_results:
            writer.writerow(row)
        writer.writerow(["average", avg_precision, avg_recall, avg_f1])

    return {
        "name": step_name.replace("Train ", ""),
        "fold_results": fold_results,
        "threshold": best_threshold,
        "avg": {"precision": avg_precision, "recall": avg_recall, "f1": avg_f1},
        "path": output_path,
    }
