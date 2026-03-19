import os
import pickle
import numpy as np
import csv
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import precision_score, recall_score, f1_score
from progress import ProgressBar


def _jaccard(text_a, text_b):
    tokens_a = set(text_a.split())
    tokens_b = set(text_b.split())
    if not tokens_a and not tokens_b:
        return 1.0
    if not tokens_a or not tokens_b:
        return 0.0
    return len(tokens_a & tokens_b) / len(tokens_a | tokens_b)


def jaccard_baseline(positive_pairs, negative_pairs, temp_dir, results_folder):
    # Load texts
    texts_cache_path = os.path.join(temp_dir, "texts_cache.pkl")
    if os.path.exists(texts_cache_path):
        print("  Loading text cache...")
        with open(texts_cache_path, "rb") as f:
            texts = pickle.load(f)
    else:
        texts = {}
        all_indices = set()
        for idx_a, idx_b in positive_pairs + negative_pairs:
            all_indices.add(idx_a)
            all_indices.add(idx_b)
        for idx in all_indices:
            with open(os.path.join(temp_dir, f"func_{idx}.txt"), "r", encoding="utf-8") as f:
                texts[idx] = f.read()

    # Compute Jaccard similarity for every pair
    print("  Computing Jaccard similarities...")
    all_pairs = positive_pairs + negative_pairs
    y = np.array([1] * len(positive_pairs) + [0] * len(negative_pairs))
    similarities = np.array([_jaccard(texts[a], texts[b]) for a, b in all_pairs])

    # 10-fold stratified CV — find optimal threshold on training fold, apply to test fold
    skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    thresholds = np.arange(0.0, 1.01, 0.01)

    fold_results = []
    progress = ProgressBar(10, ["Folds"])
    progress.status("Starting Jaccard cross-validation...")

    for fold, (train_idx, test_idx) in enumerate(skf.split(similarities.reshape(-1, 1), y), start=1):
        sim_train, y_train = similarities[train_idx], y[train_idx]
        sim_test, y_test = similarities[test_idx], y[test_idx]

        # Vectorised threshold search on training fold
        best_threshold, best_f1 = 0.5, -1.0
        for t in thresholds:
            f1 = f1_score(y_train, (sim_train >= t).astype(int), zero_division=0)
            if f1 > best_f1:
                best_f1, best_threshold = f1, t

        y_pred = (sim_test >= best_threshold).astype(int)
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

    os.makedirs(results_folder, exist_ok=True)
    output_path = os.path.join(results_folder, "jaccard_baseline_results.csv")
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["fold", "precision", "recall", "f1"])
        for row in fold_results:
            writer.writerow(row)
        writer.writerow(["average", avg_precision, avg_recall, avg_f1])

    print(f"Results saved to {output_path}")
    return fold_results
