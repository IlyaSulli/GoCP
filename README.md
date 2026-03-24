<img width="1920" height="600" alt="gocp-alt" src="https://github.com/user-attachments/assets/c542e34b-cf0f-4b18-833c-9a539d81cb9c" />

# GoCP - Graph-of-Code Python

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.55-FF4B4B?logo=streamlit&logoColor=white)
![License](https://img.shields.io/github/license/IlyaSulli/GoCP)

A Python code clone detection tool built on the **Graph-of-Code (GoC)** approach. GoCP represents each function as a dependency graph — capturing structural, control, and data-flow relationships — and uses a Random Forest classifier to detect clones across all four clone types.

Includes three baseline methods (TF-IDF full, TF-IDF keywords, Jaccard similarity) for comparison.

---

## Features

- **Graph-of-Code model** — AST-based graph with control and data dependency edges; 56-feature fingerprint
- **Three baselines** — TF-IDF (full tokens), TF-IDF (keywords only), Jaccard similarity
- **Streamlit web UI** — side-by-side Ace editors with syntax highlighting and instant clone detection
- **Multi-function support** — paste an entire file; the tool extracts and lets you pick the function
- **Optimised thresholds** — decision thresholds are tuned automatically from out-of-fold predictions during training
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
| **GoC (Graph-of-Code)** | Builds a dependency graph per function, extracts 56 graph metrics, classifies with Random Forest |
| **TF-IDF (full)** | Bag-of-words token vectors + Random Forest |
| **TF-IDF (keywords only)** | Python keyword vectors + Random Forest |
| **Jaccard similarity** | Token set overlap with a learned threshold |

---

## Retraining

```bash
python train/main.py --poolc --save-models --baseline --keyword-baseline --jaccard
```

See [manual.md](manual.md) for the full list of training options and how to adjust decision thresholds.

---

## Evaluating

```bash
python test/clone_type_eval.py
```

Runs all available models against 50 hand-crafted test cases (10 per clone type) and reports per-type accuracy.

---

## Documentation

| File | Description |
|---|---|
| [`manual.md`](manual.md) | Full usage guide — installation, app, training, evaluation, troubleshooting |
| [`replication.md`](replication.md) | Step-by-step instructions to reproduce the reported results |
| [`requirements.txt`](requirements.txt) | Python dependencies with pinned versions |

---

## Screenshots

<img width="3680" height="1792" alt="terminal" src="https://github.com/user-attachments/assets/97e5af4e-0146-4a51-886f-e6dfc0b746fa" />

<img width="3840" height="2160" alt="Screenshot 2026-03-24 101851" src="https://github.com/user-attachments/assets/ee21d94d-697d-4ea4-8c26-f2afebb91a11" />
<img width="3840" height="2160" alt="Screenshot 2026-03-24 102047" src="https://github.com/user-attachments/assets/23b7023d-95d0-4593-ad97-f575ce6a6ffc" />


