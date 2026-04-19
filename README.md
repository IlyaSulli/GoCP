<img width="1920" height="600" alt="gocp-alt" src="https://github.com/user-attachments/assets/c542e34b-cf0f-4b18-833c-9a539d81cb9c" />

# GoCP - Graph-of-Code Python

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.55-FF4B4B?logo=streamlit&logoColor=white)
![License](https://img.shields.io/github/license/IlyaSulli/GoCP)

A Python code clone detection tool built on the **Graph-of-Code (GoC)** approach. GoCP represents each function as a dependency graph — capturing structural, control, and data-flow relationships — and uses a scale-invariant Gradient Boosted Trees classifier with domain-agnostic pairwise features to detect clones across all four clone types.

Includes three baseline methods (TF-IDF full, TF-IDF keywords, Jaccard similarity) for comparison. Now supports mixing in CodeSearchNet negatives for robust, out-of-domain evaluation (see `--diverse-negatives`).

Read the research paper [here](https://github.com/IlyaSulli/GoCP/blob/main/ISE%20Research%20Paper.pdf)

---

## Features

- **Graph-of-Code model** — AST-based graph with control and data dependency edges; 56-feature fingerprint
- **Three baselines** — TF-IDF (full tokens), TF-IDF (keywords only), Jaccard similarity
- **Streamlit web UI** — side-by-side Ace editors with syntax highlighting and instant clone detection
- **Multi-function support** — paste an entire file; the tool extracts and lets you pick the function
- **Optimised thresholds** — decision thresholds are tuned on a held-out validation set during training, or fixed at 0.5 with `--fixed-threshold`
- **Clone type evaluation** — 50-case test suite covering Type-1 through Type-4 clones and false negatives

---

## Quick Start

```bash
# 1. Clone (Git LFS required for model files)
git clone https://github.com/IlyaSulli/GoCP.git
cd GoCP

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
python -m streamlit run app/app.py
```

The app opens at `http://localhost:8501`. Paste two Python functions, select a method from the sidebar, and click **Detect Clone**.

---

## Detection Methods

| Method | How it works |
|---|---|
| **GoC (Graph-of-Code)** | Dependency graph per function, 56 graph metrics, pairwise domain-agnostic features, Gradient Boosted Trees |
| **TF-IDF (full)** | Bag-of-words token vectors + Random Forest |
| **TF-IDF (keywords only)** | Python keyword vectors + Random Forest |
| **Jaccard similarity** | Token set overlap with a learned threshold |

---

## Retraining

```bash
python train/main.py --poolc -n 100000 --save-models --tfidf --tfidf-keywords --jaccard --diverse-negatives 0.7
```

---

## Training Arguments (Summary)

| Flag | Description |
|---|---|
| `--poolc` | Use PoolC dataset from Hugging Face |
| `--diverse-negatives [RATIO]` | Mix in CodeSearchNet negatives at given ratio (default 0.7) for robust negative sampling |
| `--tfidf` | Train TF-IDF (full) baseline |
| `--tfidf-keywords` | Train TF-IDF (keywords only) baseline |
| `--jaccard` | Train Jaccard baseline |
| `--save-models` | Save trained models |
| `--fixed-threshold` | Use fixed 0.5 threshold instead of learning |
| `--reprocess` | Ignore cache and reprocess data |
| `--show-errors` | Print details for failed files |
| `--log [FILE]` | Write a log file |

---

Use a fixed 0.5 threshold instead of learning it from the validation set
```
python train/main.py --poolc -n 100000 --save-models --fixed-threshold
```

See [manual.md](manual.md) for the full list of training options and how to adjust decision thresholds.

---

## Evaluating

**Clone type evaluation** — 50 hand-crafted test cases (10 per clone type):
```bash
python test/clone_type_eval.py
```

**Cross-validation metrics, Wilcoxon tests, and end-to-end timing:**
```bash
python test/eval_metrics.py
```

---

## Documentation

| File | Description |
|---|---|
| [`manual.md`](manual.md) | Full usage guide — installation, app, training, evaluation, troubleshooting |
| [`replication.md`](replication.md) | Step-by-step instructions to reproduce the reported results |
| [`requirements.txt`](requirements.txt) | Python dependencies with pinned versions |
| [`requirements.md`](requirements.md) | Dependency descriptions and compatibility notes |

---

## Screenshots

### Model Training

<img width="2048" height="1094" alt="carbon" src="https://github.com/user-attachments/assets/6876bf02-6739-4d5e-872e-77768b4abed4" />

### Type 4 Functions
The following functions have slightly different graphical representations but serve the same function. It has correctly identified that they **ARE** clone functions 

<img width="3840" height="2160" alt="Screenshot 2026-03-24 102047" src="https://github.com/user-attachments/assets/23b7023d-95d0-4593-ad97-f575ce6a6ffc" />

### Similar Functions

The following functions have a similar graphical representation but are not the same function. It has correctly identified that they are **NOT** clone functions

<img width="3840" height="2160" alt="Screenshot 2026-03-24 101851" src="https://github.com/user-attachments/assets/ee21d94d-697d-4ea4-8c26-f2afebb91a11" />



