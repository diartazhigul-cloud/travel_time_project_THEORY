import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from scipy import stats

import formula_pages
import sandbox
from analysis import fisher_ci, summarize
from cleaning import build_tables
from i18n import GROUPS, PAGES, TEXTS, TRANSPORT_LABELS, describe_r
from style import (
    BLACK,
    COLORWAY,
    CSS,
    CYAN,
    GREEN,
    PINK,
    YELLOW,
)
from ui import button, show, table
from ui import decision_box as _decision_box

ALPHA = 0.05

st.set_page_config(
    page_title="Travel Time & Attendance",
    page_icon="🕹️",
    layout="wide",
)
st.markdown(CSS, unsafe_allow_html=True)

# --------------------------------------------------------------------------
# Data and statistics
# --------------------------------------------------------------------------
@st.cache_data
def load_data():
    return build_tables()


raw_df, analysis_df = load_data()
x = analysis_df["travel_minutes"].to_numpy(dtype=float)
y = analysis_df["attendance_percent"].to_numpy(dtype=float)
n = len(analysis_df)
r, p_value = stats.pearsonr(x, y)
reg = stats.linregress(x, y)
r2 = reg.rvalue ** 2
reject = p_value < ALPHA
ci_lo, ci_hi = fisher_ci(r, n)
df_deg = n - 2
t_stat = r * np.sqrt(df_deg / (1 - r ** 2)) if abs(r) < 1 else np.nan

# --------------------------------------------------------------------------
# Session state, language, navigation
# --------------------------------------------------------------------------
ORDER = [pid for g in GROUPS for pid in g["pages"]]

if "lang" not in st.session_state:
    st.session_state.lang = "EN"
if "page" not in st.session_state or st.session_state.page not in ORDER:
    st.session_state.page = "home"


def go_to(pid):
    st.session_state.page = pid


st.sidebar.radio(
    TEXTS[st.session_state.lang]["lang_short"],
    ["EN", "RU"],
    horizontal=True,
    key="lang",
)
lang = st.session_state.lang
tr = TEXTS[lang]
page = st.session_state.page
PAGE_NAMES = dict(PAGES[lang])

st.sidebar.markdown(f"<div class='logo'>🕹️<br>{tr['logo']}</div>", unsafe_allow_html=True)

for gi, g in enumerate(GROUPS, 1):
    st.sidebar.markdown(
        f"<div class='world-title'>{g['icon']} {tr['world']} {gi} · {g['name'][lang]}</div>",
        unsafe_allow_html=True,
    )
    for pid in g["pages"]:
        active = pid == page
        mark = "►" if active else "·"
        button(
            st.sidebar,
            f"{mark} {ORDER.index(pid) + 1:02d} {PAGE_NAMES[pid]}",
            key=f"nav_{pid}",
            on_click=go_to,
            args=(pid,),
            type="primary" if active else "secondary",
        )

st.sidebar.markdown(
    f"<div class='score-box'>{tr['score']}<br>n = {n}<br>r = {r:.3f}<br>p = {p_value:.3f}</div>",
    unsafe_allow_html=True,
)

# Pretty labels
analysis_df = analysis_df.copy()
analysis_df["transport_label"] = analysis_df["transport_key"].map(lambda k: TRANSPORT_LABELS[lang].get(k, k))
raw_view = raw_df.copy()
raw_view["transport_label"] = raw_view["transport_key"].map(lambda k: TRANSPORT_LABELS[lang].get(k, k))


# --------------------------------------------------------------------------
# Reusable UI pieces
# --------------------------------------------------------------------------
def group_of(pid):
    for gi, g in enumerate(GROUPS, 1):
        if pid in g["pages"]:
            return gi, g
    return 1, GROUPS[0]


def top_hud(pid):
    idx = ORDER.index(pid) + 1
    gi, g = group_of(pid)
    cells = "".join(
        f"<i class='{'done' if k < idx else ('now' if k == idx else '')}'></i>"
        for k in range(1, len(ORDER) + 1)
    )
    st.markdown(
        f"<div class='hud'><span>{g['icon']} {tr['world']} {gi}: <b>{g['name'][lang]}</b></span>"
        f"<span>{tr['stage']} <b>{idx:02d}</b>/{len(ORDER)}</span></div>"
        f"<div class='bar'>{cells}</div>",
        unsafe_allow_html=True,
    )


def footer_nav(pid):
    i = ORDER.index(pid)
    st.markdown("---")
    c1, c2, c3 = st.columns([1, 2, 1])
    if i > 0:
        button(c1, f"◄ {tr['btn_prev']}", key="prev", on_click=go_to, args=(ORDER[i - 1],))
    if i < len(ORDER) - 1:
        nxt = ORDER[i + 1]
        c2.markdown(
            f"<div style='text-align:center'>{tr['next_up']}:<br><b style='color:{YELLOW}'>{PAGE_NAMES[nxt]}</b></div>",
            unsafe_allow_html=True,
        )
        button(c3, f"{tr['btn_next']} ►", key="next", on_click=go_to, args=(nxt,), type="primary")
    else:
        button(c3, f"↻ {tr['btn_restart']}", key="restart", on_click=go_to, args=("home",), type="primary")


def kpi_row():
    c1, c2, c3, c4 = st.columns(4)
    c1.metric(tr["metric_n"], n)
    c2.metric(tr["metric_time"], f"{analysis_df['travel_minutes'].mean():.1f} min")
    c3.metric(tr["metric_att"], f"{analysis_df['attendance_percent'].mean():.1f}%")
    c4.metric(tr["metric_r"], f"{r:.3f}")


def scatter_fig(with_line=True):
    fig = px.scatter(
        analysis_df,
        x="travel_minutes",
        y="attendance_percent",
        color="transport_label",
        color_discrete_sequence=COLORWAY,
        hover_data=["student", "year"],
        labels={
            "travel_minutes": tr["x_axis"],
            "attendance_percent": tr["y_axis"],
            "transport_label": tr["col_transport"],
        },
        title=tr["scatter_title"],
    )
    fig.update_traces(marker=dict(size=12, symbol="square", line=dict(color=BLACK, width=2)))
    if with_line:
        line_x = np.linspace(x.min(), x.max(), 100)
        line_y = reg.intercept + reg.slope * line_x
        fig.add_trace(
            go.Scatter(x=line_x, y=line_y, mode="lines", name="OLS", line=dict(color=YELLOW, width=4))
        )
    fig.update_layout(legend_title_text="")
    return fig


def style_bars(fig, color=CYAN):
    fig.update_traces(
        marker_color=color,
        marker_line_color="#ffffff",
        marker_line_width=3,
        textposition="outside",
        textfont=dict(family="Press Start 2P, monospace", size=11, color="#ffffff"),
        cliponaxis=False,
    )
    return fig


def decision_box():
    _decision_box(tr, reject)


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------
def page_home():
    st.markdown(
        f"<div class='hero'><div class='tag blink'>★ {tr['btn_start']} ★</div>"
        f"<h1>{tr['hero_title']}</h1><p>{tr['hero_lead']}</p></div>",
        unsafe_allow_html=True,
    )
    _, mid, _ = st.columns([1, 1, 1])
    button(mid, f"► {tr['btn_start']}", key="start", on_click=go_to, args=("about",), type="primary")

    st.write("")
    kpi_row()

    phrase = describe_r(r, lang)
    sentence = (tr["key_sentence_sig"] if reject else tr["key_sentence_ns"]).format(phrase=phrase, r=r, p=p_value)
    st.markdown(
        f"<div class='keyresult'><div class='lbl'>★ {tr['key_result']}</div><div class='txt'>{sentence}</div></div>",
        unsafe_allow_html=True,
    )
    show(scatter_fig())

    st.subheader(tr["home_map"])
    per_row = 4
    for start in range(0, len(GROUPS), per_row):
        cols = st.columns(per_row)
        for off, (col, g) in enumerate(zip(cols, GROUPS[start:start + per_row])):
            gi = start + off + 1
            col.markdown(
                f"<div class='worldcard'><div class='w'>{g['icon']} {tr['world']} {gi}</div>"
                f"<div class='n'>{g['name'][lang]}</div><div class='d'>{g['desc'][lang]}</div></div>",
                unsafe_allow_html=True,
            )
            button(col, f"► {tr['btn_enter']}", key=f"enter_{g['id']}", on_click=go_to, args=(g["pages"][0],))


def page_about():
    st.header(tr["about_title"])
    st.write(tr["about_body"])
    st.subheader(tr["methods_title"])
    st.markdown(tr["methods_list"])
    kpi_row()


def page_research():
    st.header(tr["rq_title"])
    st.info(tr["rq_text"])
    st.subheader(tr["variables"])
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"**{tr['x_title']}**")
        st.write(tr["x_text"])
    with c2:
        st.markdown(f"**{tr['y_title']}**")
        st.write(tr["y_text"])


def page_hypotheses():
    st.header(tr["obj_title"])
    st.write(tr["obj_text"])
    st.subheader(tr["hyp_title"])
    st.markdown(f"- **{tr['h0']}**")
    st.markdown(f"- **{tr['h1']}**")
    st.success(tr["alpha"])


def page_survey():
    st.header(tr["survey_title"])
    st.caption(tr["survey_note"])
    st.caption(
        f"{tr['metric_n']}: {len(raw_df)} · {tr['kept']}: {n} · {tr['excluded']}: {len(raw_df) - n}"
    )
    tab_all, tab_clean = st.tabs([tr["tab_all"], tr["tab_clean"]])
    with tab_all:
        table(
            raw_view[["student", "year", "travel_raw", "transport_label", "attendance_raw", "action"]].rename(
                columns={
                    "student": tr["col_student"],
                    "year": tr["col_year"],
                    "travel_raw": tr["col_travel_raw"],
                    "transport_label": tr["col_transport"],
                    "attendance_raw": tr["col_att_raw"],
                    "action": tr["col_action"],
                }
            )
        )
    with tab_clean:
        table(
            analysis_df[["student", "year", "travel_minutes", "transport_label", "attendance_percent"]].rename(
                columns={
                    "student": tr["col_student"],
                    "year": tr["col_year"],
                    "travel_minutes": tr["col_travel"],
                    "transport_label": tr["col_transport"],
                    "attendance_percent": tr["col_att"],
                }
            )
        )


def page_cleaning():
    st.header(tr["clean_title"])
    st.write(tr["clean_intro"])
    st.subheader(tr["clean_examples"])
    st.markdown("\n".join(f"- {tr[f'ex{i}']}" for i in range(1, 9)))
    examples = pd.DataFrame(
        {
            tr["raw_in"]: [
                "1 сағат",
                "1.5 сағат",
                "10-15 минут",
                "20-30 минут",
                "30-50",
                "90-100%",
                "99,90%",
                "1 мин + Самолет",
            ],
            tr["cleaned_to"]: ["60 min", "90 min", "12.5 min", "25 min", "40 min", "95%", "99.9%", tr["excluded_word"]],
            tr["rule"]: [
                tr["rule_hours"],
                tr["rule_hours"],
                tr["rule_range"],
                tr["rule_range"],
                tr["rule_range"],
                tr["rule_range"],
                tr["rule_comma"],
                tr["rule_unreal"],
            ],
        }
    )
    table(examples)
    st.subheader(tr["excluded"])
    excluded = raw_view.loc[~raw_view["keep"]]
    table(excluded[["student", "travel_raw", "transport_raw", "attendance_raw", "action"]])
    st.subheader(tr["kept"])
    table(
        analysis_df[["student", "travel_raw", "travel_minutes", "attendance_raw", "attendance_percent", "travel_note"]]
    )


def page_descriptive():
    st.header(tr["desc_title"])
    kpi_row()
    time_s = summarize(analysis_df["travel_minutes"])
    att_s = summarize(analysis_df["attendance_percent"])
    keys = ["mean", "median", "min", "max", "std", "var", "q1", "q3", "iqr"]
    labels = ["mean", "median", "minimum", "maximum", "std", "var", "q1", "q3", "iqr"]
    tbl = pd.DataFrame(
        {
            "": [tr[k] for k in labels],
            tr["var_time"]: [time_s[k] for k in keys],
            tr["var_att"]: [att_s[k] for k in keys],
        }
    ).round(2)
    table(tbl)


def page_visualization():
    st.header(tr["viz_title"])
    tab_h, tab_s, tab_b = st.tabs([tr["tab_hist"], tr["tab_scatter"], tr["tab_box"]])
    with tab_h:
        c1, c2 = st.columns(2)
        with c1:
            fig = px.histogram(
                analysis_df,
                x="travel_minutes",
                nbins=10,
                title=tr["hist_time"],
                labels={"travel_minutes": tr["x_axis"]},
            )
            fig.update_traces(marker_color=CYAN, marker_line_color="#ffffff", marker_line_width=2)
            fig.update_layout(yaxis_title=tr["count"], bargap=0.05)
            show(fig, 380)
        with c2:
            fig = px.histogram(
                analysis_df,
                x="attendance_percent",
                nbins=10,
                title=tr["hist_att"],
                labels={"attendance_percent": tr["y_axis"]},
            )
            fig.update_traces(marker_color=PINK, marker_line_color="#ffffff", marker_line_width=2)
            fig.update_layout(yaxis_title=tr["count"], bargap=0.05)
            show(fig, 380)
    with tab_s:
        show(scatter_fig(), 480)
    with tab_b:
        b1, b2 = st.columns(2)
        with b1:
            fig = px.box(
                analysis_df,
                y="travel_minutes",
                points="all",
                title=tr["var_time"],
                labels={"travel_minutes": tr["x_axis"]},
            )
            fig.update_traces(marker_color=CYAN, line_color=CYAN, fillcolor="rgba(53,224,255,0.25)")
            show(fig, 440)
        with b2:
            fig = px.box(
                analysis_df,
                y="attendance_percent",
                points="all",
                title=tr["var_att"],
                labels={"attendance_percent": tr["y_axis"]},
            )
            fig.update_traces(marker_color=PINK, line_color=PINK, fillcolor="rgba(255,79,154,0.25)")
            show(fig, 440)


def page_correlation():
    st.header(tr["corr_title"])
    phrase = describe_r(r, lang)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            f"<div class='card'><div class='lbl'>{tr['pearson']}</div>"
            f"<div class='big-r'>r = {r:.3f}</div><div class='txt'>{phrase}</div></div>",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f"<div class='card'><div class='lbl'>{tr['pvalue']}</div>"
            f"<div class='big-r'>{p_value:.3f}</div><div class='txt'>α = {ALPHA}</div></div>",
            unsafe_allow_html=True,
        )
    decision_box()
    st.write(tr["because_lt"] if reject else tr["because_gt"])
    st.caption(f"{tr['ci95']}: [{ci_lo:.3f}, {ci_hi:.3f}]")
    show(scatter_fig(), 460)


def page_regression():
    st.header(tr["reg_title"])
    st.subheader(tr["equation"])
    st.latex(rf"\text{{Attendance}} = {reg.intercept:.2f} {reg.slope:+.4f} \times \text{{Travel time}}")
    c1, c2, c3 = st.columns(3)
    c1.metric(tr["slope"], f"{reg.slope:.4f}")
    c2.metric(tr["intercept"], f"{reg.intercept:.2f}")
    c3.metric(tr["r2"], f"{r2:.3f}")
    show(scatter_fig(with_line=True), 460)


def page_testing():
    st.header(tr["test_title"])
    st.markdown(f"- **{tr['test_h0']}**")
    st.markdown(f"- **{tr['test_h1']}**")
    st.write(tr["alpha"])
    c1, c2, c3 = st.columns(3)
    c1.metric("r", f"{r:.3f}")
    c2.metric(tr["t_stat"], f"{t_stat:.3f}")
    c3.metric(tr["df"], str(df_deg))
    c4, c5 = st.columns(2)
    c4.metric(tr["pvalue"], f"{p_value:.3f}")
    c5.metric("α", str(ALPHA))
    decision_box()
    st.write(tr["because_lt"] if reject else tr["because_gt"])


def page_year():
    st.header(tr["year_title"])
    st.info(tr["year_note"])
    grouped = (
        analysis_df.groupby("year")
        .agg(attendance=("attendance_percent", "mean"), count=("student", "size"))
        .reset_index()
        .sort_values("year")
    )
    grouped["attendance"] = grouped["attendance"].round(1)
    table(grouped.rename(columns={"year": tr["col_year"], "attendance": tr["col_att"], "count": tr["n_group"]}))
    fig = px.bar(
        grouped,
        x="year",
        y="attendance",
        text="attendance",
        title=tr["year_mean"],
        labels={"year": tr["col_year"], "attendance": tr["col_att"]},
    )
    style_bars(fig, YELLOW)
    fig.update_traces(texttemplate="%{text:.1f}%")
    fig.update_xaxes(type="category")
    fig.update_yaxes(range=[0, 115])
    show(fig)


def page_transport():
    st.header(tr["transport_title"])
    st.info(tr["transport_note"])
    grouped = (
        analysis_df.groupby("transport_label")
        .agg(attendance=("attendance_percent", "mean"), count=("student", "size"))
        .reset_index()
        .sort_values("attendance", ascending=False)
    )
    grouped["attendance"] = grouped["attendance"].round(1)
    table(
        grouped.rename(
            columns={"transport_label": tr["col_transport"], "attendance": tr["col_att"], "count": tr["n_group"]}
        )
    )
    fig = px.bar(
        grouped,
        x="attendance",
        y="transport_label",
        orientation="h",
        text="attendance",
        title=tr["transport_title"],
        labels={"attendance": tr["col_att"], "transport_label": tr["col_transport"]},
    )
    style_bars(fig, GREEN)
    fig.update_traces(texttemplate="%{text:.1f}%")
    fig.update_xaxes(range=[0, 120])
    fig.update_yaxes(autorange="reversed")
    show(fig)


def page_bins():
    st.header(tr["bins_title"])
    st.write(tr["bins_note"])
    order = ["0–15", "16–30", "31–60", "61+"]
    grouped = (
        analysis_df.groupby("travel_bin")
        .agg(attendance=("attendance_percent", "mean"), count=("student", "size"))
        .reindex(order)
        .dropna()
        .reset_index()
    )
    grouped["attendance"] = grouped["attendance"].round(1)
    table(grouped.rename(columns={"travel_bin": tr["x_axis"], "attendance": tr["col_att"], "count": tr["n_group"]}))
    fig = px.bar(
        grouped,
        x="travel_bin",
        y="attendance",
        text="attendance",
        category_orders={"travel_bin": order},
        labels={"travel_bin": tr["x_axis"], "attendance": tr["col_att"]},
    )
    style_bars(fig, PINK)
    fig.update_traces(texttemplate="%{text:.1f}%")
    fig.update_yaxes(range=[0, 115])
    show(fig)


def page_interpretation():
    st.header(tr["interp_title"])
    st.write(tr["interp_r"])
    st.markdown(f"**r = {r:.3f}** → {describe_r(r, lang)}")
    st.markdown(f"**p = {p_value:.3f}**, α = {ALPHA}")
    st.write(tr["because_lt"] if reject else tr["because_gt"])
    st.warning(tr["causation"])
    st.write(tr["interp_extra"])


def page_limitations():
    st.header(tr["lim_title"])
    st.markdown(tr["lim_list"])
    st.info(tr["lim_cause"])
    st.markdown(
        "<div class='pixel-ascii'>Travel time ──► Attendance\n"
        "Schedule, motivation, workload, health, transport reliability ──► Attendance</div>",
        unsafe_allow_html=True,
    )


def page_conclusion():
    st.header(tr["conc_title"])
    c1, c2, c3, c4 = st.columns(4)
    c1.metric(tr["sample_size"], n)
    c2.metric("Pearson r", f"{r:.3f}")
    c3.metric(tr["pvalue"], f"{p_value:.3f}")
    c4.metric("α", str(ALPHA))
    st.write("")
    decision_box()
    st.success(tr["conc_yes"] if reject else tr["conc_no"])
    st.caption(tr["footer"])


PAGE_FUNCS = {
    "home": page_home,
    "about": page_about,
    "research": page_research,
    "hypotheses": page_hypotheses,
    "survey": page_survey,
    "cleaning": page_cleaning,
    "descriptive": page_descriptive,
    "visualization": page_visualization,
    "correlation": page_correlation,
    "regression": page_regression,
    "testing": page_testing,
    "year": page_year,
    "transport": page_transport,
    "bins": page_bins,
    "interpretation": page_interpretation,
    "limitations": page_limitations,
    "conclusion": page_conclusion,
}

def _formula_page(pid):
    return lambda: formula_pages.render(pid, PAGE_NAMES[pid], tr, lang, analysis_df)


for _pid in formula_pages.TRY:
    PAGE_FUNCS[_pid] = _formula_page(_pid)
PAGE_FUNCS["user_data"] = lambda: sandbox.render(PAGE_NAMES["user_data"], tr, lang, analysis_df)
assert all(p in PAGE_FUNCS for p in ORDER), "page without a function"

top_hud(page)
PAGE_FUNCS[page]()
footer_nav(page)
