"""Small UI helpers shared by all pages."""
import re

import streamlit as st

from style import retro_fig

_VER = tuple(int(p) for p in re.findall(r"\d+", st.__version__)[:2])


def _wide(fn, *args, **kwargs):
    """Call a Streamlit widget so it fills the width (new and old Streamlit versions)."""
    if _VER >= (1, 50):
        try:
            return fn(*args, width="stretch", **kwargs)
        except Exception:
            pass
    return fn(*args, use_container_width=True, **kwargs)


def table(df):
    _wide(st.dataframe, df, hide_index=True)


def show(fig, height=420):
    retro_fig(fig, height)
    _wide(st.plotly_chart, fig, theme=None)


def button(container, label, **kwargs):
    return _wide(container.button, label, **kwargs)


def formula(label, latex, note=None):
    """Formula card: green label, LaTeX in a pixel frame, optional hint."""
    st.markdown(f"<div class='flabel'>{label}</div>", unsafe_allow_html=True)
    st.latex(latex)
    if note:
        st.caption(note)


def result(label, value):
    """One 'score line': label on the left, value on the right."""
    st.markdown(f"<div class='result'><span>{label}</span><b>{value}</b></div>", unsafe_allow_html=True)


def decision_box(tr, reject):
    klass = "ok" if reject else "warn"
    decision = tr["reject"] if reject else tr["fail"]
    st.markdown(f"<div class='decision {klass}'>{decision}</div>", unsafe_allow_html=True)
