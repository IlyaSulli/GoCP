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
python train/main.py --poolc --save-models --baseline --keyword-baseline --jaccard --sample 200000
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
python train/main.py --poolc --save-models --baseline --keyword-baseline --jaccard --sample 200000 --fixed-threshold
```

> **Note:** The first run downloads and processes the dataset. Subsequent runs reuse the cache in `temp/` and are significantly faster.

---

## Expected Results

The following results should be reproduced (averaged across 10 folds):

| Method | Precision | Recall | F1 |
|---|---|---|---|
| **GoC (Graph-of-Code)** | 0.7499 | 0.7884 | 0.7686 |
| **TF-IDF (full)** | 0.8720 | 0.8606 | 0.8662 |
| **TF-IDF (keywords only)** | 0.7319 | 0.7168 | 0.7242 |
| **Jaccard similarity** | 0.6417 | 0.7766 | 0.7027 |

Statistical comparison (GoC vs TF-IDF full, Wilcoxon signed-rank test):

| Metric | Value |
|---|---|
| GoC average F1 | 0.7686 |
| TF-IDF (full) average F1 | 0.8662 |
| Wilcoxon W | 0.0000 |
| p-value | 0.0020 |
| Effect size (r) | 0.9794 |

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
python train/main.py --poolc --save-models --baseline --keyword-baseline --jaccard -n 10000
```

Results will differ from the reported values but the relative ordering of methods should remain consistent.
