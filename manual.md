# GoCP — Graph-of-Code Python: User Manual

## Overview

GoCP is a Python code clone detection tool that identifies whether two Python functions are clones of each other. It implements the **Graph-of-Code (GoC)** approach, which represents each function as a dependency graph and extracts structural features for classification, alongside three baseline methods for comparison.

**Four detection methods are available:**

| Method | Approach | Best For |
|---|---|---|
| GoC (Graph-of-Code) | AST graph + Random Forest | All clone types, especially Type-3/4 |
| TF-IDF (full) | Token vectors + Random Forest | General similarity |
| TF-IDF (keywords only) | Keyword vectors + Random Forest | Structural similarity |
| Jaccard similarity | Token set overlap | Quick approximation |

---

## System Requirements

- Python 3.10 or later
- Git with Git LFS (for cloning model files)
- ~500 MB disk space (for models)
- Internet connection (only needed for retraining on PoolC dataset)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/IlyaSulli/GoCP.git
cd GoCP
```

> Git LFS is required to download the pre-trained model files. If you do not have it installed, download it from https://git-lfs.com and run `git lfs install` before cloning.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

If no `requirements.txt` is present, install manually:

```bash
pip install streamlit streamlit-ace networkx scikit-learn scipy numpy joblib datasets
```

### 3. Verify models are present

```bash
ls models/
```

You should see:

```
goc_model.joblib
tfidf_full_model.joblib
tfidf_keyword_model.joblib
jaccard_model.joblib
```

If any are missing, see the [Retraining Models](#retraining-models) section.

---

## Quick Start

Launch the web application:

```bash
python -m streamlit run app/app.py
```

A browser window will open at `http://localhost:8501`. Paste two Python functions into the editors, select a detection method from the sidebar, and click **Detect Clone**.

---

## Web Application

### Starting the app

```bash
python -m streamlit run app/app.py
```

### Interface

**Sidebar (Settings)**

- **Detection method** — choose from GoC, TF-IDF (full), TF-IDF (keywords only), or Jaccard similarity. Only methods with trained model files are shown.
- **Editor theme** — choose a syntax highlighting theme (monokai, github, tomorrow_night, solarized_dark, dracula, xcode).

**Main area**

- **Function A / Function B** — paste one Python function into each editor. The editor supports syntax highlighting, line numbers, and standard keyboard shortcuts.
- If you paste a file with multiple functions, a dropdown will appear allowing you to select which function to use.
- Click **Detect Clone** to run detection.

**Results**

- **Clone detected** (green) or **Not a clone** (blue) verdict.
- **Clone probability** (or Jaccard similarity) score between 0.0 and 1.0.
- A progress bar giving a visual representation of the score.

### Tips

- Functions do not need to be at the top level — indented code (e.g. copied from inside a class) is automatically dedented before processing.
- Python 2 syntax is automatically converted to Python 3 before analysis.
- The decision threshold for each method is set automatically during training. To override it, see [Adjusting the Decision Threshold](#adjusting-the-decision-threshold).

---

## Retraining Models

To retrain all models from scratch using the PoolC dataset (requires an internet connection to download from Hugging Face):

```bash
python train/main.py --poolc --save-models --tfidf --tfidf-keywords --jaccard
```

**Data source options:**

| Flag | Short | Description |
|---|---|---|
| `--poolc` | | Load data from the PoolC Hugging Face dataset instead of `--data` |
| `--data DIR` | | Path to a local data folder (default: `./data/`) |
| `--sample N` | `-n N` | Number of pairs to sample from PoolC (default: 20000) |

**Method options:**

| Flag | Description |
|---|---|
| `--no-goc` | Skip the GoCP classifier |
| `--tfidf` | Train the TF-IDF (full tokens) model |
| `--tfidf-keywords` | Train the TF-IDF (keywords only) model |
| `--jaccard` | Train the Jaccard similarity baseline |

**Output options:**

| Flag | Short | Description |
|---|---|---|
| `--save-models` | | Save trained models to `--models` folder |
| `--results DIR` | `-r DIR` | Folder to write results CSV files (default: `./results/`) |
| `--models DIR` | `-m DIR` | Folder to write model files (default: `./models/`) |

**Misc options:**

| Flag | Short | Description |
|---|---|---|
| `--fixed-threshold` | | Use a fixed 0.5 decision threshold instead of learning it from the validation set |
| `--reprocess` | | Ignore cached data and reprocess from scratch |
| `--show-errors` | `-v` | Print details for files that failed to process |
| `--log [FILE]` | | Write a log file; FILE defaults to `<results>/gocp.log` if not given |
| `--diverse-negatives [RATIO]` | | Mix in CodeSearchNet (general Python) negatives at the given ratio (default `0.7`); reduces same-domain false positives — only applies with `--poolc` |

**Example — train GoC only on 50,000 pairs:**

```bash
python train/main.py --poolc --save-models -n 50000
```

**Example — retrain all models, forcing reprocessing:**

```bash
python train/main.py --poolc --save-models --tfidf --tfidf-keywords --jaccard --reprocess
```

**Example — retrain with a fixed 0.5 threshold:**

```bash
python train/main.py --poolc --save-models --tfidf --tfidf-keywords --jaccard --fixed-threshold
```

> **Note:** If you change the dataset size, delete `temp/features_cache.npz` first. Otherwise the cached features from the previous run will be reused regardless of `--sample`.

Training outputs a per-fold precision, recall, and F1 score for each method, and prints the decision threshold (either learned from the held-out validation set or fixed at 0.5).

---

## Adjusting the Decision Threshold

Each model has a decision threshold saved inside it. By default, training finds the threshold that maximises F1 on a held-out validation set (15% of training data). You can instead use a fixed 0.5 threshold by passing `--fixed-threshold` at training time. To override the threshold of an already-trained model without retraining:

```bash
python set_threshold.py <model> <threshold>
```

| Model name | File |
|---|---|
| `goc` | `models/goc_model.joblib` |
| `tfidf` | `models/tfidf_full_model.joblib` |
| `tfidf-keywords` | `models/tfidf_keyword_model.joblib` |
| `jaccard` | `models/jaccard_model.joblib` |

**Example — raise GoC threshold to 0.65 to reduce false positives:**

```bash
python set_threshold.py goc 0.65
```

The change takes effect immediately on the next app restart. No retraining is needed.

To check the current threshold without changing it:

```bash
python -c "import joblib; m = joblib.load('models/goc_model.joblib'); print(m.get('threshold'))"
```

---

## Running the Evaluation Suite

To evaluate all available models against the 50-case clone type test suite:

```bash
python test/clone_type_eval.py
```

This tests 10 cases per clone type:

- **Type-1** — exact clones (whitespace/comment differences only)
- **Type-2** — renamed identifiers (variable and function names changed)
- **Type-3** — gapped clones (statements added, removed, or reordered)
- **Type-4** — semantic clones (same logic, different implementation)
- **False** — non-clones (should be rejected)

Results are printed to the terminal showing pass/fail per case, per-type accuracy, and overall accuracy per method.

---

## Project Structure

```
GoCP/
├── app/
│   ├── app.py              # Streamlit web application
│   ├── predictor.py        # Model loading and prediction
│   └── scanner.py          # AST-based function extractor
├── models/                 # Trained model files (.joblib)
├── src/
│   ├── goc.py              # Graph-of-Code construction
│   ├── features.py         # 56-feature graph fingerprint
│   └── preprocess.py       # Source code preprocessing
├── train/
│   ├── main.py             # Training entry point
│   ├── classifier.py       # GoCP + RandomForest trainer
│   ├── baseline.py         # TF-IDF trainer
│   └── jaccard_baseline.py # Jaccard trainer
├── test/
│   └── clone_type_eval.py  # Clone type evaluation suite
├── results/                # Training results (CSV)
├── set_threshold.py        # Threshold override utility
├── manual.md               # This file
├── replication.md          # Replication instructions
└── requirements.txt        # Python dependencies
```

---

## Troubleshooting

**`streamlit: command not found`**

Run using the Python module flag:
```bash
python -m streamlit run app/app.py
```

**`Model file not found: models/goc_model.joblib`**

Either Git LFS did not download the files, or they have not been trained yet. Run:
```bash
git lfs pull
```
Or retrain using the command in [Retraining Models](#retraining-models).

**`Prediction failed: unexpected indent`**

The pasted code has leading indentation. The app handles this automatically via `textwrap.dedent` — if you still see this, ensure the code is valid Python syntax.

**Getting the same results after retraining with more data**

Delete the features cache before retraining:
```bash
rm temp/features_cache.npz
```

**High false positive rate**

The models are trained on competitive programming code (PoolC), where non-clone pairs can still share structural patterns. Raise the GoC threshold to reduce false positives:
```bash
python set_threshold.py goc 0.65
```
