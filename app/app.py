import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st
from streamlit_ace import st_ace
from scanner import extract_functions
from predictor import available_methods, predict

st.set_page_config(page_title="GoCP — Graph-of-Code Python", layout="wide")

st.title("GoCP — Graph-of-Code Python")
st.caption("Paste two Python functions below and select a detection method.")

# ── Method selector ────────────────────────────────────────────────────────────

methods = available_methods()

if not methods:
    st.error(
        "No trained models found in the `models/` folder.\n\n"
        "Train them first by running:\n"
        "```\npython train/main.py --poolc --save-models --baseline "
        "--keyword-baseline --jaccard\n```"
    )
    st.stop()

# ── Sidebar ────────────────────────────────────────────────────────────────────

with st.sidebar:
    st.header("Settings")

    method = st.selectbox("Detection method", methods)

    ace_theme = st.selectbox(
        "Editor theme",
        ["monokai", "github", "tomorrow_night", "solarized_dark", "dracula", "xcode"],
        index=0,
    )

# ── Code input ─────────────────────────────────────────────────────────────────

col1, col2 = st.columns(2)

ACE_PLACEHOLDER_A = "def foo(x):\n    return x + 1\n"
ACE_PLACEHOLDER_B = "def bar(n):\n    return n + 1\n"

ACE_COMMON = dict(
    language="python",
    theme=ace_theme,
    font_size=14,
    tab_size=4,
    show_gutter=True,
    show_print_margin=False,
    wrap=False,
    auto_update=True,
    height=300,
)

with col1:
    st.subheader("Function A")
    code_a = st_ace(value=ACE_PLACEHOLDER_A, key="code_a", **ACE_COMMON)

with col2:
    st.subheader("Function B")
    code_b = st_ace(value=ACE_PLACEHOLDER_B, key="code_b", **ACE_COMMON)

# ── Function selector (if multiple functions pasted) ──────────────────────────

def pick_function(code: str, label: str) -> str | None:
    if not code.strip():
        return None
    funcs = extract_functions(code)
    if len(funcs) == 1:
        return funcs[0][1]
    names = [name for name, _ in funcs]
    choice = st.selectbox(f"Multiple functions found in {label} — select one:", names, key=f"sel_{label}")
    return dict(funcs)[choice]


selected_a = pick_function(code_a, "Function A")
selected_b = pick_function(code_b, "Function B")

# ── Predict ────────────────────────────────────────────────────────────────────

st.divider()

if st.button("Detect Clone", type="primary", use_container_width=True):
    if not selected_a:
        st.warning("Please paste a function in the Function A box.")
    elif not selected_b:
        st.warning("Please paste a function in the Function B box.")
    else:
        with st.spinner(f"Running {method}..."):
            try:
                label, score = predict(method, selected_a, selected_b)
            except FileNotFoundError as e:
                st.error(str(e))
                st.stop()
            except Exception as e:
                st.error(f"Prediction failed: {e}")
                st.stop()

        if label == 1:
            st.success(f"**Clone detected** ({method})")
        else:
            st.info(f"**Not a clone** ({method})")

        score_label = "Jaccard similarity" if "Jaccard" in method else "Clone probability"
        st.metric(score_label, f"{score:.4f}")
        st.progress(min(score, 1.0))

