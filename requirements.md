# GoCP — Requirements

## Python

Python **3.10 or later** is required. Tested on Python 3.14.3 (Windows 11).

## Dependencies

All dependencies are listed in [`requirements.txt`](requirements.txt) with pinned versions.

| Package | Version | Purpose |
|---|---|---|
| `datasets` | 4.8.2 | Hugging Face dataset loading (PoolC, CodeSearchNet) |
| `joblib` | 1.5.3 | Model serialisation (save/load `.joblib` files) |
| `networkx` | 3.6.1 | Graph construction and graph-theoretic metric computation |
| `numpy` | 2.4.3 | Numerical operations, feature arrays, statistical summaries |
| `pandas` | 2.3.3 | Results CSV handling |
| `scikit-learn` | 1.8.0 | HistGradientBoostingClassifier, RandomForestClassifier, cross-validation, TF-IDF vectorisation |
| `scipy` | 1.17.1 | Wilcoxon signed-rank tests, sparse matrix operations |
| `streamlit` | 1.55.0 | Web application framework |
| `streamlit-ace` | 0.1.1 | Ace code editor component for the Streamlit UI |

## Installation

```bash
pip install -r requirements.txt
```

## Other

| Tool | Purpose |
|---|---|
| Git LFS | Required to clone pre-trained model files from the repository |
| Internet access | Required only for downloading datasets during training |
