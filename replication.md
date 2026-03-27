# GoCP — Replication Instructions

This document explains how to reproduce the experimental results reported in the paper.

---

## Environment

| Requirement | Version |
|---|---|
| Python | 3.10 or later |
| Operating system | Windows / Linux / macOS |
| Internet access | Required (PoolC dataset downloaded from Hugging Face) |
| Git LFS | Required (model files stored via LFS) |

Install all Python dependencies:

```bash
pip install -r requirements.txt
```

---

## Reproducing Training Results

The reported results were produced by training on **200,000 pairs** (100,000 positive, 100,000 negative) sampled from the [PoolC dataset](https://huggingface.co/datasets/AhmedSSoliman/PoolC) via Hugging Face.

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
python train/main.py --poolc --save-models --tfidf --tfidf-keywords --jaccard --sample 200000
```

This will:
1. Download and preprocess 200,000 pairs from PoolC (~20–40 minutes depending on hardware)
2. Train all four models with 10-fold stratified cross-validation
3. Print per-fold and average Precision / Recall / F1 for each method
4. Find and print the optimal decision threshold from a held-out validation set (15% of training data)
5. Save trained models to `models/`
6. Save per-fold results to `results/`

To use a fixed 0.5 threshold instead of learning it, add `--fixed-threshold`:

```bash
python train/main.py --poolc --save-models --tfidf --tfidf-keywords --jaccard --sample 200000 --fixed-threshold
```

> **Note:** The first run downloads and processes the dataset. Subsequent runs reuse the cache in `temp/` and are significantly faster.

---

## Expected Results


The following results should be reproduced for GoCP (10-fold CV, with diverse negatives):

| Fold | Precision | Recall | F1 |
|---|---|---|---|
| 1 | 0.837 | 0.947 | 0.889 |
| 2 | 0.847 | 0.947 | 0.894 |
| 3 | 0.844 | 0.943 | 0.891 |
| 4 | 0.846 | 0.949 | 0.895 |
| 5 | 0.839 | 0.943 | 0.888 |
| 6 | 0.836 | 0.943 | 0.887 |
| 7 | 0.844 | 0.946 | 0.892 |
| 8 | 0.841 | 0.951 | 0.893 |
| 9 | 0.856 | 0.952 | 0.901 |
| 10 | 0.842 | 0.947 | 0.892 |
| **Average** | **0.843** | **0.947** | **0.892** |

See [results/gocp_results.csv](results/gocp_results.csv) for raw output.


Raw per-fold results are saved to `results/` as CSV files and can be compared directly with the versions already in the repository.

> **Note:** Due to the random sampling from PoolC and random seed usage in RandomForest, results may vary slightly between runs. The reported averages should be reproducible to within ±0.005 F1.

---

## Reproducing the Clone Type Evaluation

After training, run the 50-case clone type evaluation:

```bash
python test/clone_type_eval.py
```

This tests all available models against 10 hand-crafted cases per clone type (Type-1, Type-2, Type-3, Type-4, and False negatives) and prints per-type and overall pass rates.

---

## Reproducing with a Different Sample Size

To replicate a smaller run (e.g. for a faster test):

```bash
rm temp/features_cache.npz   # or del on Windows
python train/main.py --poolc --save-models --tfidf --tfidf-keywords --jaccard -n 10000
```

Results will differ from the reported values but the relative ordering of methods should remain consistent.
