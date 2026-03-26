import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import csv
import pickle
import numpy as np
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


def jaccard_baseline(positive_pairs, negative_pairs, temp_dir, results_folder, models_folder=None, pipeline=None):
    texts_cache_path = os.path.join(temp_dir, "texts_cache.pkl")
    if os.path.exists(texts_cache_path):
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

    all_pairs = positive_pairs + negative_pairs
    y = np.array([1] * len(positive_pairs) + [0] * len(negative_pairs))

    total_steps = 10 + (1 if models_folder else 0)

    if pipeline is not None:
        pipeline.begin("Train Jaccard", total_steps, ["Folds"])
        progress = pipeline
    else:
        progress = ProgressBar(total_steps, ["Folds"])

    progress.status("Computing Jaccard similarities...")
    similarities = np.array([_jaccard(texts[a], texts[b]) for a, b in all_pairs])

    skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    thresholds = np.linspace(0.0, 1.0, 101)

    fold_results = []
    for fold, (train_idx, test_idx) in enumerate(skf.split(similarities.reshape(-1, 1), y), start=1):
        progress.status(f"Fold {fold}/10: Evaluating...")
        sim_train, y_train = similarities[train_idx], y[train_idx]
        sim_test, y_test = similarities[test_idx], y[test_idx]

        best_threshold, best_f1 = 0.5, -1.0
        for t in thresholds:
            f1 = f1_score(y_train, (sim_train >= t).astype(int), zero_division=0)
            if f1 > best_f1:
                best_f1, best_threshold = f1, t

        y_pred = (sim_test >= best_threshold).astype(int)
        precision = precision_score(y_test, y_pred, zero_division=0)
        recall    = recall_score(y_test, y_pred, zero_division=0)
        f1        = f1_score(y_test, y_pred, zero_division=0)

        fold_results.append((fold, precision, recall, f1))
        progress.update("Folds")

    avg_precision = np.mean([r[1] for r in fold_results])
    avg_recall    = np.mean([r[2] for r in fold_results])
    avg_f1        = np.mean([r[3] for r in fold_results])

    saved_threshold = 0.6  # fixed deployment threshold for Jaccard

    model_path = None
    if models_folder:
        import joblib
        os.makedirs(models_folder, exist_ok=True)
        progress.status("Saving Jaccard model...")
        model_path = os.path.join(models_folder, "jaccard_model.joblib")
        joblib.dump({"threshold": saved_threshold}, model_path)
        progress.update("Folds")

    progress.finish()

    os.makedirs(results_folder, exist_ok=True)
    output_path = os.path.join(results_folder, "jaccard_baseline_results.csv")
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["fold", "precision", "recall", "f1"])
        for row in fold_results:
            writer.writerow(row)
        writer.writerow(["average", avg_precision, avg_recall, avg_f1])

    return {
        "name": "Jaccard",
        "fold_results": fold_results,
        "threshold": saved_threshold,
        "avg": {"precision": avg_precision, "recall": avg_recall, "f1": avg_f1},
        "path": output_path,
    }
