"""
Manually override the decision threshold saved in a model file.

Usage:
    python set_threshold.py goc 0.65
    python set_threshold.py tfidf 0.60
    python set_threshold.py tfidf-keywords 0.60
    python set_threshold.py jaccard 0.45
"""
import sys
import os
import joblib

MODELS_DIR = os.path.join(os.path.dirname(__file__), "models")

MODEL_FILES = {
    "goc":           "goc_model.joblib",
    "tfidf":         "tfidf_full_model.joblib",
    "tfidf-keywords": "tfidf_keyword_model.joblib",
    "jaccard":       "jaccard_model.joblib",
}

if len(sys.argv) != 3:
    print(__doc__)
    sys.exit(1)

name, value = sys.argv[1], sys.argv[2]

if name not in MODEL_FILES:
    print(f"Unknown model '{name}'. Choose from: {', '.join(MODEL_FILES)}")
    sys.exit(1)

try:
    threshold = float(value)
    if not 0.0 <= threshold <= 1.0:
        raise ValueError
except ValueError:
    print("Threshold must be a float between 0.0 and 1.0")
    sys.exit(1)

path = os.path.join(MODELS_DIR, MODEL_FILES[name])
if not os.path.exists(path):
    print(f"Model file not found: {path}")
    sys.exit(1)

model = joblib.load(path)
old = model.get("threshold", "not set")
model["threshold"] = threshold
joblib.dump(model, path)

print(f"{MODEL_FILES[name]}: threshold {old} -> {threshold}")
