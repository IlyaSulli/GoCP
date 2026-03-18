import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.feature_extraction.text import TfidfVectorizer
import csv
from progress import ProgressBar


def baseline(positive_pairs, negative_pairs, temp_dir, results_folder):
    total_pairs = len(positive_pairs) + len(negative_pairs)
    prep = ProgressBar(3, ["Done"])

    # Step 1: Load raw function text for each unique function index
    prep.status("Loading text files...")
    all_indices = set()
    for idx_a, idx_b in positive_pairs + negative_pairs:
        all_indices.add(idx_a)
        all_indices.add(idx_b)

    texts = {}
    for idx in all_indices:
        with open(os.path.join(temp_dir, f"func_{idx}.txt"), "r", encoding="utf-8") as f:
            texts[idx] = f.read()
    prep.update("Done")

    # Step 2: Fit TF-IDF on all function texts
    prep.status("Fitting TF-IDF vectorizer...")
    vectorizer = TfidfVectorizer(analyzer="word", token_pattern=r"[A-Za-z_]\w*|\S", max_features=5000)
    all_texts = [texts[idx] for idx in sorted(all_indices)]
    vectorizer.fit(all_texts)
    prep.update("Done")

    # Step 3: Transform all texts and build dataset
    prep.status(f"Building feature matrix for {total_pairs} pairs...")
    tfidf_cache = {idx: vectorizer.transform([texts[idx]]).toarray()[0] for idx in all_indices}

    X = []
    y = []

    for idx_a, idx_b in positive_pairs:
        vec_a, vec_b = tfidf_cache[idx_a], tfidf_cache[idx_b]
        X.append(np.concatenate([vec_a, vec_b, np.abs(vec_a - vec_b)]))
        y.append(1)

    for idx_a, idx_b in negative_pairs:
        vec_a, vec_b = tfidf_cache[idx_a], tfidf_cache[idx_b]
        X.append(np.concatenate([vec_a, vec_b, np.abs(vec_a - vec_b)]))
        y.append(0)

    X = np.array(X)
    y = np.array(y)
    prep.update("Done")
    prep.finish()

    # 10-fold stratified cross-validation (same splits as GoC for fair comparison)
    skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)

    fold_results = []
    progress = ProgressBar(10, ["Folds"])
    progress.status("Starting baseline cross-validation...")

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
    output_path = os.path.join(results_folder, "baseline_results.csv")

    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["fold", "precision", "recall", "f1"])
        for row in fold_results:
            writer.writerow(row)
        writer.writerow(["average", avg_precision, avg_recall, avg_f1])

    print(f"Results saved to {output_path}")
