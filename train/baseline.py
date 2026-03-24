import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import csv
import pickle
import numpy as np
from scipy import sparse
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.feature_extraction.text import TfidfVectorizer
from progress import ProgressBar


_PYTHON_KEYWORDS_PATTERN = (
    r"\b(?:False|None|True|and|as|assert|async|await|break|class|continue|"
    r"def|del|elif|else|except|finally|for|from|global|if|import|in|is|"
    r"lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)\b"
)


def baseline(positive_pairs, negative_pairs, temp_dir, results_folder, keyword_only=False, models_folder=None):
    all_indices = set()
    for idx_a, idx_b in positive_pairs + negative_pairs:
        all_indices.add(idx_a)
        all_indices.add(idx_b)

    texts_cache_path = os.path.join(temp_dir, "texts_cache.pkl")
    if os.path.exists(texts_cache_path):
        print("  Loading text cache...")
        with open(texts_cache_path, "rb") as f:
            texts = pickle.load(f)
    else:
        texts = {}
        load_progress = ProgressBar(len(all_indices), ["Loaded"])
        load_progress.status("Loading text files...")
        for idx in all_indices:
            with open(os.path.join(temp_dir, f"func_{idx}.txt"), "r", encoding="utf-8") as f:
                texts[idx] = f.read()
            load_progress.update("Loaded")
        load_progress.finish()

    label = "Keyword-only TF-IDF" if keyword_only else "TF-IDF"
    token_pattern = _PYTHON_KEYWORDS_PATTERN if keyword_only else r"[A-Za-z_]\w*|\S"
    print(f"  Fitting {label} vectorizer...")
    all_idx_list = sorted(all_indices)
    vectorizer = TfidfVectorizer(analyzer="word", token_pattern=token_pattern, max_features=2000)
    vectorizer.fit([texts[idx] for idx in all_idx_list])

    print("  Building feature matrix...")
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

    skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)

    fold_results = []
    progress = ProgressBar(10, ["Folds"])
    progress.status(f"Starting {label} cross-validation...")

    for fold, (train_idx, test_idx) in enumerate(skf.split(X, y), start=1):
        progress.status(f"Fold {fold}/10: Training...")
        clf.fit(X[train_idx], y[train_idx])
        progress.status(f"Fold {fold}/10: Evaluating...")
        probs = clf.predict_proba(X[test_idx])[:, 1]
        y_pred = (probs >= 0.5).astype(int)
        precision = precision_score(y[test_idx], y_pred, zero_division=0)
        recall    = recall_score(y[test_idx], y_pred, zero_division=0)
        f1        = f1_score(y[test_idx], y_pred, zero_division=0)
        fold_results.append((fold, precision, recall, f1))
        progress.update("Folds")

    progress.finish()

    best_threshold = 0.6

    avg_precision = np.mean([r[1] for r in fold_results])
    avg_recall    = np.mean([r[2] for r in fold_results])
    avg_f1        = np.mean([r[3] for r in fold_results])
    print(f"  {'Average':8s}: Precision={avg_precision:.4f}  Recall={avg_recall:.4f}  F1={avg_f1:.4f}")

    os.makedirs(results_folder, exist_ok=True)
    filename = "keyword_baseline_results.csv" if keyword_only else "baseline_results.csv"
    output_path = os.path.join(results_folder, filename)
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["fold", "precision", "recall", "f1"])
        for row in fold_results:
            writer.writerow(row)
        writer.writerow(["average", avg_precision, avg_recall, avg_f1])
    print(f"Results saved to {output_path}")

    if models_folder:
        import joblib
        os.makedirs(models_folder, exist_ok=True)
        model_name = "tfidf_keyword_model.joblib" if keyword_only else "tfidf_full_model.joblib"
        print(f"  Training final {label} model on all data...")
        final_clf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
        final_clf.fit(X, y)
        model_path = os.path.join(models_folder, model_name)
        joblib.dump({"vectorizer": vectorizer, "clf": final_clf, "keyword_only": keyword_only, "threshold": best_threshold}, model_path)
        print(f"  Saved to {model_path}")

    return fold_results
