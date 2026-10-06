"""Sandbox page: players add their own data and everything is recalculated."""
import uuid

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

import storage
from analysis import analyze, summarize
from i18n import TRANSPORT_LABELS, describe_r
from style import BLACK, CYAN, GREEN, PINK, YELLOW
from ui import button, decision_box, show, table

TRANSPORT_CHOICES = ["walk", "bus", "car", "walk_bus", "other"]
MAX_PER_PLAYER = 25
ALPHA = 0.05


def _sid():
    if "sid" not in st.session_state:
        st.session_state["sid"] = uuid.uuid4().hex[:8]
    return st.session_state["sid"]


def _delete_selected(sid):
    ids = st.session_state.get("ud_del_ids", [])
    if ids:
        storage.delete_rows(ids, sid)
    st.session_state["ud_del_ids"] = []


def _clear_mine(sid):
    storage.delete_session(sid)
    st.session_state["ud_del_ids"] = []


def render(title, tr, lang, survey_df):
    sid = _sid()
    names = TRANSPORT_LABELS[lang]

    st.header(title)
    st.write(tr["ud_intro"])
    st.caption(tr["ud_privacy"])

    # ------------------------------------------------------------ 1. add
    st.subheader(tr["ud_step1"])
    player_df = storage.load_player_data()
    mine_count = int((player_df["session"] == sid).sum())

    with st.form("ud_form", clear_on_submit=False):
        c1, c2, c3 = st.columns(3)
        year = c1.selectbox(tr["ud_year"], [1, 2, 3, 4], key="ud_year")
        transport = c2.selectbox(
            tr["ud_transport"], TRANSPORT_CHOICES, format_func=lambda k: names[k], key="ud_transport"
        )
        attendance = c3.number_input(
            tr["ud_att"], min_value=0.0, max_value=100.0, value=90.0, step=1.0, key="ud_att_val"
        )
        c4, c5 = st.columns([2, 1])
        travel = c4.number_input(
            tr["ud_travel"], min_value=0.0, max_value=600.0, value=30.0, step=1.0, key="ud_travel_val"
        )
        unit = c5.selectbox(
            tr["ud_unit"],
            ["min", "h"],
            format_func=lambda u: tr["ud_unit_min"] if u == "min" else tr["ud_unit_h"],
            key="ud_unit_val",
        )
        submitted = st.form_submit_button(f"★ {tr['ud_submit']}")

    if submitted:
        minutes = travel * 60 if unit == "h" else travel
        if mine_count >= MAX_PER_PLAYER:
            st.error(tr["ud_limit"].format(n=MAX_PER_PLAYER))
        elif not (1 <= minutes <= 300):
            st.error(tr["ud_bad_travel"])
        elif storage.append_row(sid, year, minutes, transport, attendance) is None:
            st.error(tr["ud_full"])
        else:
            st.success(tr["ud_added"])
            player_df = storage.load_player_data()

    # ------------------------------------------------------------ 2. data
    st.subheader(tr["ud_step2"])
    st.caption(tr["ud_players_count"].format(n=len(player_df)))
    scope = st.radio(
        tr["ud_scope"],
        ["survey_players", "players", "mine"],
        format_func=lambda k: tr[f"ud_scope_{k}"],
        horizontal=True,
        key="ud_scope",
    )

    survey_part = survey_df[["student", "year", "travel_minutes", "transport_key", "attendance_percent"]].copy()
    survey_part["student"] = "S" + survey_part["student"].astype(str)
    survey_part["source"] = tr["ud_src_survey"]

    players = player_df.copy()
    players["student"] = "P" + players["id"].astype(str)
    players["source"] = np.where(players["session"] == sid, tr["ud_src_me"], tr["ud_src_players"])
    cols = ["student", "year", "travel_minutes", "transport_key", "attendance_percent", "source"]
    players = players[cols]

    if scope == "survey_players":
        data = pd.concat([survey_part[cols], players], ignore_index=True) if len(players) else survey_part[cols]
    elif scope == "players":
        data = players
    else:
        data = players[players["source"] == tr["ud_src_me"]]
    data = data.reset_index(drop=True)
    data["transport_label"] = data["transport_key"].map(lambda k: names.get(k, k))

    table(
        data[["student", "source", "year", "travel_minutes", "transport_label", "attendance_percent"]].rename(
            columns={
                "student": tr["col_student"],
                "source": tr["ud_col_source"],
                "year": tr["col_year"],
                "travel_minutes": tr["col_travel"],
                "transport_label": tr["col_transport"],
                "attendance_percent": tr["col_att"],
            }
        )
    )

    # my entries
    mine = player_df[player_df["session"] == sid]
    st.markdown(f"**{tr['ud_mine']}**")
    if mine.empty:
        st.caption(tr["ud_none_mine"])
    else:
        valid = set(mine["id"].tolist())
        st.session_state["ud_del_ids"] = [i for i in st.session_state.get("ud_del_ids", []) if i in valid]
        lookup = {
            int(r.id): f"#{int(r.id)} · {r.travel_minutes:g} min · {r.attendance_percent:g}%"
            for r in mine.itertuples()
        }
        st.multiselect(tr["ud_delete_pick"], list(lookup), format_func=lambda i: lookup[i], key="ud_del_ids")
        b1, b2 = st.columns(2)
        button(b1, tr["ud_delete"], key="ud_del_btn", on_click=_delete_selected, args=(sid,))
        button(b2, tr["ud_clear"], key="ud_clear_btn", on_click=_clear_mine, args=(sid,))

    # ------------------------------------------------------------ 3. results
    st.subheader(tr["ud_step3"])
    n = len(data)
    if n == 0:
        st.info(tr["ud_empty"])
        return

    res = analyze(data["travel_minutes"], data["attendance_percent"])
    base = analyze(survey_df["travel_minutes"], survey_df["attendance_percent"])

    k1, k2, k3, k4 = st.columns(4)
    k1.metric(tr["metric_n"], n)
    k2.metric(tr["metric_time"], f"{data['travel_minutes'].mean():.1f} min")
    k3.metric(tr["metric_att"], f"{data['attendance_percent'].mean():.1f}%")
    k4.metric(tr["metric_r"], f"{res['r']:.3f}" if res else "—")

    fig = px.scatter(
        data,
        x="travel_minutes",
        y="attendance_percent",
        color="source",
        color_discrete_map={
            tr["ud_src_survey"]: CYAN,
            tr["ud_src_players"]: PINK,
            tr["ud_src_me"]: GREEN,
        },
        hover_data=["student", "year"],
        labels={
            "travel_minutes": tr["x_axis"],
            "attendance_percent": tr["y_axis"],
            "source": tr["ud_col_source"],
        },
        title=tr["scatter_title"],
    )
    fig.update_traces(marker=dict(size=12, symbol="square", line=dict(color=BLACK, width=2)))
    if res:
        lx = np.linspace(data["travel_minutes"].min(), data["travel_minutes"].max(), 100)
        fig.add_trace(
            go.Scatter(
                x=lx, y=res["intercept"] + res["slope"] * lx, mode="lines", name="OLS", line=dict(color=YELLOW, width=4)
            )
        )
    fig.update_layout(legend_title_text="")
    show(fig, 460)

    if res is None:
        st.warning(tr["ud_need_more"])
        return

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            f"<div class='card'><div class='lbl'>{tr['pearson']}</div>"
            f"<div class='big-r'>r = {res['r']:.3f}</div><div class='txt'>{describe_r(res['r'], lang)}</div></div>",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f"<div class='card'><div class='lbl'>{tr['pvalue']}</div>"
            f"<div class='big-r'>{res['p']:.3f}</div><div class='txt'>α = {ALPHA}</div></div>",
            unsafe_allow_html=True,
        )
    decision_box(tr, res["reject"])
    st.write(tr["because_lt"] if res["reject"] else tr["because_gt"])
    st.caption(f"{tr['ci95']}: [{res['ci_lo']:.3f}, {res['ci_hi']:.3f}]")
    if n < 10:
        st.caption(tr["ud_small"])

    st.subheader(tr["equation"])
    st.latex(
        rf"\text{{Attendance}} = {res['intercept']:.2f} {res['slope']:+.4f} \times \text{{Travel time}}"
    )
    m1, m2, m3 = st.columns(3)
    m1.metric(tr["slope"], f"{res['slope']:.4f}")
    m2.metric(tr["intercept"], f"{res['intercept']:.2f}")
    m3.metric(tr["r2"], f"{res['r2']:.3f}")

    # survey only vs selected data
    st.subheader(tr["ud_compare"])
    if base:
        rows = [
            (tr["sample_size"], f"{base['n']}", f"{res['n']}"),
            (tr["metric_time"], f"{survey_df['travel_minutes'].mean():.1f}", f"{data['travel_minutes'].mean():.1f}"),
            (tr["metric_att"], f"{survey_df['attendance_percent'].mean():.1f}", f"{data['attendance_percent'].mean():.1f}"),
            ("r", f"{base['r']:.3f}", f"{res['r']:.3f}"),
            (tr["pvalue"], f"{base['p']:.3f}", f"{res['p']:.3f}"),
            (tr["slope"], f"{base['slope']:.4f}", f"{res['slope']:.4f}"),
            (tr["intercept"], f"{base['intercept']:.2f}", f"{res['intercept']:.2f}"),
            (tr["r2"], f"{base['r2']:.3f}", f"{res['r2']:.3f}"),
        ]
        table(
            pd.DataFrame(
                {
                    tr["ud_col_metric"]: [r[0] for r in rows],
                    tr["ud_col_survey"]: [r[1] for r in rows],
                    tr["ud_col_sel"]: [r[2] for r in rows],
                }
            )
        )

    # descriptive statistics of the selected data
    if n >= 2:
        st.subheader(tr["desc_title"])
        ts, as_ = summarize(data["travel_minutes"]), summarize(data["attendance_percent"])
        keys = ["mean", "median", "min", "max", "std", "var", "q1", "q3", "iqr"]
        labels = ["mean", "median", "minimum", "maximum", "std", "var", "q1", "q3", "iqr"]
        table(
            pd.DataFrame(
                {
                    "": [tr[k] for k in labels],
                    tr["var_time"]: [ts[k] for k in keys],
                    tr["var_att"]: [as_[k] for k in keys],
                }
            ).round(2)
        )

    csv = data.drop(columns=["transport_label"]).to_csv(index=False).encode("utf-8")
    st.download_button(tr["ud_download"], csv, file_name="selected_data.csv", mime="text/csv", key="ud_dl")
