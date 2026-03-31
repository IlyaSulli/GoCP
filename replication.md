# GoCP — Replication Instructions

This document explains how to reproduce the experimental results reported in the paper.

---

## Environment

| Requirement | Version |
|---|---|
| Python | 3.10 or later |
| Operating system | Windows / Linux / macOS |
| Internet access | Required (PoolC and CodeSearchNet datasets downloaded from Hugging Face) |
| Git LFS | Required (model files stored via LFS) |

Install all Python dependencies:

```bash
pip install -r requirements.txt
```

---

## Reproducing Training Results

The reported results were produced by training on **100,000 pairs** (~50,000 positive, ~50,000 negative) sampled from the [PoolC dataset](https://huggingface.co/datasets/PoolC/1-fold-clone-detection-600k-5fold), with 70% of negative pairs drawn from [CodeSearchNet](https://huggingface.co/datasets/code-search-net/code_search_net) to reduce same-domain bias.

### Step 1 — Clear any existing cache

If you have previously run training, delete the features cache to ensure a clean run:

```bash
rm temp/features_cache.npz
```

On Windows:

```bash
del temp\features_cache.npz
```

### Step 2 — Run training

```bash
python train/main.py --poolc --save-models --tfidf --tfidf-keywords --jaccard --sample 100000 --diverse-negatives 0.7
```

This will:
1. Download and preprocess 100,000 pairs from PoolC and CodeSearchNet (~20–40 minutes depending on hardware)
2. Train all four models with 10-fold stratified cross-validation
3. Print per-fold and average Precision / Recall / F1 for each method
4. Find and print the optimal decision threshold from a held-out validation set (15% of training data)
5. Save trained models to `models/`
6. Save per-fold results to `results/`

To use a fixed 0.5 threshold instead of learning it, add `--fixed-threshold`:

```bash
python train/main.py --poolc --save-models --tfidf --tfidf-keywords --jaccard --sample 100000 --diverse-negatives 0.7 --fixed-threshold
```

> **Note:** The first run downloads and processes the dataset. Subsequent runs reuse the cache in `temp/` and are significantly faster.

---

## Expected Results

The following cross-validation results should be reproduced (10-fold stratified, with diverse negatives):

| Model | Accuracy | Precision | Recall | F1 | AUC-ROC |
|---|---|---|---|---|---|
| GoCP (Graph-of-Code) | 0.8864 ± 0.0032 | 0.8556 ± 0.0037 | 0.9306 ± 0.0045 | 0.8915 ± 0.0030 | 0.9510 ± 0.0014 |
| TF-IDF (Full) | 0.8707 ± 0.0029 | 0.8585 ± 0.0026 | 0.9962 ± 0.0011 | 0.9222 ± 0.0016 | 0.9582 ± 0.0021 |
| TF-IDF (Keywords) | 0.8196 ± 0.0044 | 0.8326 ± 0.0026 | 0.9581 ± 0.0030 | 0.8909 ± 0.0027 | 0.8219 ± 0.0063 |
| Jaccard Similarity | 0.7693 ± 0.0000 | 0.7693 ± 0.0000 | 1.0000 ± 0.0000 | 0.8696 ± 0.0000 | 0.7618 ± 0.0057 |

Raw per-fold results are saved to `results/` as CSV files and can be compared directly with the versions already in the repository.

> **Note:** Due to the random sampling from PoolC and random seed usage, results may vary slightly between runs. The reported averages should be reproducible to within ±0.005 on each metric.

---

## Reproducing the Evaluation Metrics

After training, run the full evaluation suite which includes cross-validation metrics, pairwise Wilcoxon signed-rank tests, and end-to-end prediction timing:

```bash
python test/eval_metrics.py
```

Expected Wilcoxon results (accuracy):
- GoCP vs all baselines: W = 0.00, p = 0.0020, r = 0.98 (GoCP wins)

Expected end-to-end timing (per pair):

| Model | Mean (ms) | Std (ms) |
|---|---|---|
| GoCP (Graph-of-Code) | ~110 | ~39 |
| TF-IDF (Full) | ~147 | ~4 |
| TF-IDF (Keywords) | ~143 | ~6 |
| Jaccard Similarity | ~0.2 | ~0.03 |

> **Note:** Timing results vary by hardware. The relative ordering (Jaccard fastest, GoCP faster than TF-IDF) should be consistent.

---

## Reproducing the Clone Type Evaluation

After training, run the 50-case clone type evaluation:

```bash
python test/clone_type_eval.py
```

This tests all available models against 10 hand-crafted cases per clone type (Type-1, Type-2, Type-3, Type-4, and false pairs) and prints per-type and overall pass rates.

Expected results:

| Clone Type | GoCP | TF-IDF (Full) | TF-IDF (Keywords) | Jaccard |
|---|---|---|---|---|
| Type-1 | 10/10 | 10/10 | 10/10 | 9/10 |
| Type-2 | 10/10 | 10/10 | 10/10 | 1/10 |
| Type-3 | 6/10 | 10/10 | 10/10 | 10/10 |
| Type-4 | 4/10 | 10/10 | 10/10 | 0/10 |
| False | 4/10 | 0/10 | 0/10 | 10/10 |
| **Overall** | **34/50** | **40/50** | **40/50** | **30/50** |

---

## Reproducing with a Different Sample Size

To replicate a smaller run (e.g. for a faster test):

```bash
rm temp/features_cache.npz   # or del on Windows
python train/main.py --poolc --save-models --tfidf --tfidf-keywords --jaccard -n 10000 --diverse-negatives 0.7
```

Results will differ from the reported values but the relative ordering of methods should remain consistent.
