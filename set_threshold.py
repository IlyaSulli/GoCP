"""
Manually override the decision threshold saved in a model file.
"""
import os
import shutil
import sys
import tempfile

import joblib

MODELS_DIR = os.path.join(os.path.dirname(__file__), "models")

MODEL_FILES = {
    "goc":            "goc_model.joblib",
    "tfidf":          "tfidf_full_model.joblib",
    "tfidf-keywords": "tfidf_keyword_model.joblib",
    "jaccard":        "jaccard_model.joblib",
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
old = model.get("threshold", None)
old_str = f"{old:.4f}" if isinstance(old, float) else "not set"
model["threshold"] = threshold

# Write to a temporary file first, then rename atomically to avoid
# corrupting the model file if the process is interrupted mid-write.
tmp_fd, tmp_path = tempfile.mkstemp(dir=MODELS_DIR, suffix=".tmp")
try:
    os.close(tmp_fd)
    joblib.dump(model, tmp_path)
    shutil.move(tmp_path, path)
except Exception:
    if os.path.exists(tmp_path):
        os.unlink(tmp_path)
    raise

print(f"{MODEL_FILES[name]}: threshold {old_str} -> {threshold:.4f}")
