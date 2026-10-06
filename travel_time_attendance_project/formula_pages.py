"""Pages of the 'Formulas' world: formula sheet + interactive 'Try it' tab for every topic."""
import math

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from analysis import summarize
from formulas import BLOCKS, PAGE_INFO, UI
from i18n import TRANSPORT_LABELS
from style import CYAN, PINK, YELLOW
from ui import formula, result, show, table


def big(x):
    return f"{x:,}" if x < 10 ** 12 else f"{x:.3e}"


def fmt_set(s):
    return "{" + ", ".join(str(i) for i in sorted(s)) + "}" if s else "∅"


# ---------------------------------------------------------------- school
def try_school(T, tr, lang, df):
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader(T["pct_title"])
        a = st.number_input(T["attended"], min_value=0, max_value=1000, value=36, step=1, key="sc_a")
        b = st.number_input(T["total"], min_value=1, max_value=1000, value=40, step=1, key="sc_b")
        if a > b:
            st.warning(T["a_gt_b"])
        else:
            result("p = a / b · 100%", f"{a / b * 100:.1f}%")
    with c2:
        st.subheader(T["speed_title"])
        s = st.number_input(T["distance"], min_value=0.1, max_value=500.0, value=10.0, step=0.5, key="sc_s")
        v = st.number_input(T["speed"], min_value=0.1, max_value=200.0, value=30.0, step=1.0, key="sc_v")
        hours = s / v
        result("t = s / v", f"{hours:.2f} h")
        result("t · 60", f"{hours * 60:.0f} min")
    with c3:
        st.subheader(T["mid_title"])
        lo = st.number_input(T["from"], value=10.0, step=1.0, key="sc_lo")
        hi = st.number_input(T["to"], value=15.0, step=1.0, key="sc_hi")
        result("m = (a + b) / 2", f"{(lo + hi) / 2:g}")


# ---------------------------------------------------------------- week 1
OMEGA = list(range(1, 13))


def try_sets(T, tr, lang, df):
    st.subheader(T["event_lab"])
    st.caption(T["event_lab_note"])
    c1, c2 = st.columns(2)
    A = set(c1.multiselect("A", OMEGA, default=[1, 2, 3, 4, 5], key="ev_A"))
    B = set(c2.multiselect("B", OMEGA, default=[4, 5, 6, 7], key="ev_B"))
    W = set(OMEGA)
    n = len(W)
    rows = [
        ("A ∪ B", A | B),
        ("A ∩ B", A & B),
        ("A \\ B", A - B),
        ("A^c", W - A),
        ("B^c", W - B),
        ("A^c ∩ B^c", (W - A) & (W - B)),
    ]
    table(
        pd.DataFrame(
            {
                T["col_event"]: [r[0] for r in rows],
                T["col_set"]: [fmt_set(r[1]) for r in rows],
                "m": [len(r[1]) for r in rows],
                "P = m / n": [f"{len(r[1])}/{n} = {len(r[1]) / n:.3f}" for r in rows],
            }
        )
    )
    ok = len(A | B) == len(A) + len(B) - len(A & B)
    result(
        "|A ∪ B| = |A| + |B| − |A ∩ B|",
        f"{len(A | B)} = {len(A)} + {len(B)} − {len(A & B)} ✔" if ok else "✘",
    )
    result(T["de_morgan"], "✔" if (W - (A | B)) == ((W - A) & (W - B)) else "✘")
    if not (A & B):
        st.info(T["incompatible"])

    st.subheader(T["comb_calc"])
    c1, c2 = st.columns(2)
    n_ = c1.number_input("n", min_value=0, max_value=30, value=10, step=1, key="cb_n")
    k_ = c2.number_input("k", min_value=0, max_value=30, value=3, step=1, key="cb_k")
    if k_ > n_:
        st.warning(T["k_gt_n"])
        return
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("n!", big(math.factorial(n_)))
    m2.metric("A(n, k)", big(math.perm(n_, k_)))
    m3.metric("C(n, k)", big(math.comb(n_, k_)))
    m4.metric("n^k", big(n_ ** k_))
    result(T["guess"], f"1 / {big(math.comb(n_, k_))} = {1 / math.comb(n_, k_):.6f}")


# ---------------------------------------------------------------- week 2
def try_prob(T, tr, lang, df):
    st.subheader(T["pa_calc"])
    c1, c2, c3 = st.columns(3)
    pa = c1.number_input("P(A)", min_value=0.0, max_value=1.0, value=0.5, step=0.01, format="%.2f", key="pb_a")
    pb = c2.number_input("P(B)", min_value=0.0, max_value=1.0, value=0.4, step=0.01, format="%.2f", key="pb_b")
    pab = c3.number_input("P(A ∩ B)", min_value=0.0, max_value=1.0, value=0.2, step=0.01, format="%.2f", key="pb_ab")
    lo, hi = max(0.0, pa + pb - 1), min(pa, pb)
    if pab < lo - 1e-9 or pab > hi + 1e-9:
        st.error(T["pab_range"].format(lo=lo, hi=hi))
    else:
        union = pa + pb - pab
        rows = [
            ("P(A ∪ B)", "P(A) + P(B) − P(A ∩ B)", union),
            ("P(A^c)", "1 − P(A)", 1 - pa),
            ("P(B^c)", "1 − P(B)", 1 - pb),
            ("P(A \\ B)", "P(A) − P(A ∩ B)", pa - pab),
            ("P(B \\ A)", "P(B) − P(A ∩ B)", pb - pab),
            ("P(A^c ∩ B^c)", "1 − P(A ∪ B)", 1 - union),
        ]
        table(
            pd.DataFrame(
                {
                    T["col_event"]: [r[0] for r in rows],
                    T["col_formula"]: [r[1] for r in rows],
                    T["col_value"]: [round(max(r[2], 0.0), 4) for r in rows],
                }
            )
        )

    st.subheader(T["geo_calc"])
    st.caption(T["geo_note"])
    c1, c2 = st.columns(2)
    period = c1.number_input(T["bus_period"], min_value=1, max_value=120, value=15, step=1, key="geo_T")
    wait = c2.number_input(T["bus_wait"], min_value=0, max_value=120, value=5, step=1, key="geo_w")
    w = min(wait, period)
    result("P(wait ≤ w) = w / T", f"{w}/{period} = {w / period:.3f}")


# ---------------------------------------------------------------- week 3
def try_cond(T, tr, lang, df):
    st.subheader(T["cond_calc"])
    c1, c2 = st.columns(2)
    pab = c1.number_input("P(A ∩ B)", min_value=0.0, max_value=1.0, value=0.2, step=0.01, format="%.2f", key="cd_ab")
    pb = c2.number_input("P(B)", min_value=0.0, max_value=1.0, value=0.4, step=0.01, format="%.2f", key="cd_b")
    if pb <= 0:
        st.warning(T["pb_zero"])
    elif pab > pb + 1e-9:
        st.error(T["ab_gt_b"])
    else:
        result("P(A | B) = P(A ∩ B) / P(B)", f"{pab / pb:.3f}")

    st.subheader(T["tp_survey"])
    st.caption(T["tp_survey_note"])
    thr = st.slider(T["att_thr"], min_value=50, max_value=100, value=90, step=5, key="cd_thr")
    d = df.copy()
    d["hit"] = d["attendance_percent"] >= thr
    n = len(d)
    g = d.groupby("transport_key").agg(n_i=("hit", "size"), k_i=("hit", "sum")).reset_index()
    g["p_b"] = g["n_i"] / n
    g["p_a_b"] = g["k_i"] / g["n_i"]
    g["prod"] = g["p_b"] * g["p_a_b"]
    names = TRANSPORT_LABELS[lang]
    table(
        pd.DataFrame(
            {
                T["col_hyp"]: g["transport_key"].map(lambda k: names.get(k, k)),
                "n_i": g["n_i"],
                T["col_k"]: g["k_i"].astype(int),
                "P(B_i)": g["p_b"].round(3),
                "P(A | B_i)": g["p_a_b"].round(3),
                "P(B_i) · P(A | B_i)": g["prod"].round(3),
            }
        )
    )
    k_total = int(d["hit"].sum())
    result("Σ P(B_i) · P(A | B_i)", f"{g['prod'].sum():.3f}")
    result(T["direct"], f"{k_total}/{n} = {k_total / n:.3f}")

    st.subheader(T["tp_manual"])
    defaults_b = [0.5, 0.3, 0.2]
    defaults_a = [0.9, 0.7, 0.5]
    pbs, pas = [], []
    for i, col in enumerate(st.columns(3), 1):
        with col:
            pbs.append(
                st.number_input(
                    f"P(B{i})", min_value=0.0, max_value=1.0, value=defaults_b[i - 1], step=0.05, format="%.2f", key=f"tp_b{i}"
                )
            )
            pas.append(
                st.number_input(
                    f"P(A | B{i})", min_value=0.0, max_value=1.0, value=defaults_a[i - 1], step=0.05, format="%.2f", key=f"tp_a{i}"
                )
            )
    if abs(sum(pbs) - 1) > 1e-6:
        st.error(T["sum_not_one"].format(s=sum(pbs)))
    else:
        total = sum(b * a for b, a in zip(pbs, pas))
        result("P(A) = Σ P(B_i) · P(A | B_i)", f"{total:.4f}")
        result("P(A^c) = 1 − P(A)", f"{1 - total:.4f}")


# ---------------------------------------------------------------- week 4
def try_indep(T, tr, lang, df):
    st.subheader(T["ind_calc"])
    c1, c2 = st.columns(2)
    pa = c1.number_input("P(A)", min_value=0.0, max_value=1.0, value=0.6, step=0.01, format="%.2f", key="in_a")
    pb = c2.number_input("P(B)", min_value=0.0, max_value=1.0, value=0.5, step=0.01, format="%.2f", key="in_b")
    rows = [
        ("P(A ∩ B)", "P(A) · P(B)", pa * pb),
        ("P(A ∪ B)", "P(A) + P(B) − P(A) · P(B)", pa + pb - pa * pb),
        ("P(A ∩ B^c)", "P(A) · (1 − P(B))", pa * (1 - pb)),
        ("P(A^c ∩ B)", "(1 − P(A)) · P(B)", (1 - pa) * pb),
        ("P(A^c ∩ B^c)", "(1 − P(A)) · (1 − P(B))", (1 - pa) * (1 - pb)),
    ]
    table(
        pd.DataFrame(
            {
                T["col_event"]: [r[0] for r in rows],
                T["col_formula"]: [r[1] for r in rows],
                T["col_value"]: [round(r[2], 4) for r in rows],
            }
        )
    )

    st.subheader(T["atleast"])
    st.caption(T["atleast_note"])
    c1, c2 = st.columns(2)
    p = c1.slider("p", min_value=0.01, max_value=0.99, value=0.10, step=0.01, key="in_p")
    n = c2.slider("n", min_value=1, max_value=50, value=10, step=1, key="in_n")
    now = 1 - (1 - p) ** n
    result("P = 1 − (1 − p)^n", f"{now:.4f}")
    xs = list(range(1, 51))
    ys = [1 - (1 - p) ** k for k in xs]
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=xs, y=ys, mode="lines+markers", line=dict(color=YELLOW, width=3), marker=dict(symbol="square", size=6, color=YELLOW))
    )
    fig.add_trace(
        go.Scatter(x=[n], y=[now], mode="markers", marker=dict(symbol="square", size=15, color=PINK, line=dict(color="#ffffff", width=2)))
    )
    fig.update_layout(title=T["atleast_chart"], xaxis_title="n", yaxis_title="P", showlegend=False)
    fig.update_yaxes(range=[0, 1.05])
    show(fig, 360)

    st.subheader(T["ind_survey"])
    st.caption(T["ind_survey_note"])
    c1, c2 = st.columns(2)
    t_thr = c1.slider(T["travel_thr"], min_value=5, max_value=120, value=30, step=5, key="in_t")
    a_thr = c2.slider(T["att_thr"], min_value=50, max_value=100, value=90, step=5, key="in_att")
    A = df["travel_minutes"] >= t_thr
    B = df["attendance_percent"] >= a_thr
    pA, pB, pAB = float(A.mean()), float(B.mean()), float((A & B).mean())
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("P(A)", f"{pA:.3f}")
    m2.metric("P(B)", f"{pB:.3f}")
    m3.metric("P(A ∩ B)", f"{pAB:.3f}")
    m4.metric("P(A) · P(B)", f"{pA * pB:.3f}")
    if A.sum() > 0:
        result(T["cond_vs"], f"{pAB / pA:.3f}  vs  {pB:.3f}")
    if abs(pAB - pA * pB) <= 0.05:
        st.success(T["close_indep"])
    else:
        st.warning(T["far_indep"])


# ---------------------------------------------------------------- week 5
def try_data(T, tr, lang, df):
    st.subheader(T["freq_title"])
    var = st.selectbox(
        T["variable"],
        ["travel_minutes", "attendance_percent"],
        format_func=lambda k: tr["var_time"] if k == "travel_minutes" else tr["var_att"],
        key="fd_var",
    )
    label = tr["var_time"] if var == "travel_minutes" else tr["var_att"]
    x = df[var].astype(float)
    n = len(x)
    sturges = int(round(1 + 3.322 * math.log10(n)))
    k = st.slider(T["classes"], min_value=3, max_value=12, value=min(max(sturges, 3), 12), step=1, key="fd_k")
    st.caption(T["sturges_hint"].format(k=sturges))

    xmin, xmax = float(x.min()), float(x.max())
    if xmax == xmin:
        st.info(T["constant"])
        return
    h = (xmax - xmin) / k
    edges = np.linspace(xmin, xmax, k + 1)
    counts, _ = np.histogram(x, bins=edges)
    mids = (edges[:-1] + edges[1:]) / 2
    w = counts / n
    labels = [f"[{edges[i]:.1f}; {edges[i + 1]:.1f}" + ("]" if i == k - 1 else ")") for i in range(k)]
    table(
        pd.DataFrame(
            {
                T["col_class"]: labels,
                T["col_mid"]: mids.round(2),
                "n_i": counts,
                "w_i": w.round(3),
                "F_i": np.cumsum(w).round(3),
                "f_i = n_i / (n·h)": (counts / (n * h)).round(4),
            }
        )
    )
    result("n  ·  h = (max − min) / k", f"{n}  ·  {h:.2f}")

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=mids,
            y=counts,
            width=h * 0.92,
            marker=dict(color=CYAN, line=dict(color="#ffffff", width=2)),
            name=T["bars"],
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[mids[0] - h, *mids, mids[-1] + h],
            y=[0, *counts, 0],
            mode="lines+markers",
            line=dict(color=YELLOW, width=3),
            marker=dict(symbol="square", size=9, color=YELLOW),
            name=T["polygon"],
        )
    )
    fig.update_layout(title=T["freq_chart"], xaxis_title=label, yaxis_title=tr["count"], bargap=0.05)
    show(fig, 420)

    grouped_mean = float((counts * mids).sum() / n)
    result(T["grouped_mean"], f"{grouped_mean:.2f}  vs  {x.mean():.2f}")

    st.subheader(T["desc_title2"])
    s = summarize(x)
    vc = x.value_counts()
    mode_txt = "—" if vc.max() == 1 else ", ".join(f"{m:g}" for m in sorted(vc[vc == vc.max()].index))
    cv = s["std"] / s["mean"] * 100 if s["mean"] else float("nan")
    stats_rows = [
        (tr["mean"], s["mean"]),
        (tr["median"], s["median"]),
        (T["mode"], mode_txt),
        (tr["minimum"], s["min"]),
        (tr["maximum"], s["max"]),
        (T["range"], s["max"] - s["min"]),
        (tr["var"], s["var"]),
        (tr["std"], s["std"]),
        (tr["q1"], s["q1"]),
        (tr["q3"], s["q3"]),
        (tr["iqr"], s["iqr"]),
        (T["cv"], cv),
    ]
    table(
        pd.DataFrame(
            {
                T["col_stat"]: [r[0] for r in stats_rows],
                T["col_value"]: [r[1] if isinstance(r[1], str) else f"{r[1]:.2f}" for r in stats_rows],
            }
        )
    )

    lo, hi = s["q1"] - 1.5 * s["iqr"], s["q3"] + 1.5 * s["iqr"]
    result(T["fences"] + "  [Q1 − 1.5·IQR; Q3 + 1.5·IQR]", f"[{lo:.1f}; {hi:.1f}]")
    out = df.loc[(x < lo) | (x > hi), ["student", var]]
    if out.empty:
        st.success(T["no_outliers"])
    else:
        st.warning(T["outliers_found"])
        table(out.rename(columns={"student": tr["col_student"], var: label}))


TRY = {
    "f_school": try_school,
    "f_sets": try_sets,
    "f_prob": try_prob,
    "f_cond": try_cond,
    "f_indep": try_indep,
    "f_data": try_data,
}


def render(pid, title, tr, lang, df):
    T = UI[lang]
    info = PAGE_INFO[pid]
    st.header(title)
    tag = f"{T['week']} {info['week']}" if info["week"] else T["school"]
    st.markdown(
        f"<div class='weektag'>{tag}</div><div class='topic'>{info['topic'][lang]}</div>",
        unsafe_allow_html=True,
    )
    tab_f, tab_p = st.tabs([f"📜 {T['tab_formulas']}", f"🎮 {T['tab_try']}"])
    with tab_f:
        for block_title, items in BLOCKS[pid]:
            st.subheader(block_title[lang])
            for lab, latex, note in items:
                formula(lab[lang], latex, note[lang] if note else None)
    with tab_p:
        TRY[pid](T, tr, lang, df)
