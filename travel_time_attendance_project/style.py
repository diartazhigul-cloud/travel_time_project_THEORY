"""Retro-game look: CSS for Streamlit and a matching Plotly theme."""

# Palette (arcade / 8-bit)
BG = "#120a2a"
PANEL = "#241747"
GRID = "#3b2a6b"
TEXT = "#f4f0ff"
YELLOW = "#ffd23f"
CYAN = "#35e0ff"
PINK = "#ff4f9a"
GREEN = "#5dff7a"
ORANGE = "#ff9f43"
BLACK = "#0a0518"

COLORWAY = [CYAN, PINK, YELLOW, GREEN, ORANGE, "#b388ff"]

CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&display=swap');

:root {{
  --bg: {BG}; --panel: {PANEL}; --grid: {GRID}; --text: {TEXT};
  --yellow: {YELLOW}; --cyan: {CYAN}; --pink: {PINK}; --green: {GREEN};
  --black: {BLACK};
  --pixel: 'Press Start 2P', 'Courier New', monospace;
  --body: 'VT323', 'Courier New', monospace;
}}

/* ---------- base ---------- */
.stApp {{
  background-color: var(--bg);
  background-image:
    linear-gradient(var(--grid) 1px, transparent 1px),
    linear-gradient(90deg, var(--grid) 1px, transparent 1px);
  background-size: 32px 32px;
  background-position: -1px -1px;
  color: var(--text);
  font-family: var(--body);
}}
/* CRT scanlines */
.stApp::after {{
  content: ""; position: fixed; inset: 0; pointer-events: none; z-index: 99999;
  background: repeating-linear-gradient(0deg, rgba(0,0,0,0.16) 0px, rgba(0,0,0,0.16) 1px, transparent 1px, transparent 3px);
}}
header[data-testid="stHeader"] {{ background: transparent; }}
footer, #MainMenu {{ visibility: hidden; }}
.block-container {{ padding-top: 2.2rem; max-width: 1200px; }}

.stApp p, .stApp li, .stApp label, .stApp td, .stApp th,
.stApp [data-testid="stMarkdownContainer"], .stApp [data-testid="stCaptionContainer"] {{
  font-family: var(--body);
  font-size: 1.45rem;
  line-height: 1.25;
}}
.stApp [data-testid="stCaptionContainer"] p {{ font-size: 1.2rem; color: #b9a9e6; }}

h1, h2, h3, h4 {{
  font-family: var(--pixel) !important;
  color: var(--yellow) !important;
  line-height: 1.5 !important;
  letter-spacing: 0;
  text-shadow: 3px 3px 0 var(--black);
}}
h1 {{ font-size: 1.5rem !important; }}
h2 {{ font-size: 1.15rem !important; }}
h3 {{ font-size: 0.95rem !important; color: var(--cyan) !important; }}
code {{ font-family: var(--body) !important; font-size: 1.3rem; color: var(--green); background: var(--black); border-radius: 0; padding: 0 .3rem; }}

/* ---------- sidebar ---------- */
[data-testid="stSidebar"] {{
  background: var(--black);
  border-right: 4px solid var(--grid);
}}
[data-testid="stSidebar"] .block-container, [data-testid="stSidebarUserContent"] {{ padding-top: 1rem; }}
.logo {{
  font-family: var(--pixel); color: var(--yellow); font-size: 0.8rem; line-height: 1.6;
  border: 4px solid var(--yellow); box-shadow: 4px 4px 0 var(--pink);
  padding: .7rem .8rem; margin: 0 0 1rem 0; text-align: center; background: var(--panel);
}}
.world-title {{
  font-family: var(--pixel); font-size: 0.6rem; color: var(--cyan);
  margin: 1.1rem 0 .4rem 0; padding-bottom: .3rem; border-bottom: 3px dashed var(--grid);
}}
.score-box {{
  font-family: var(--pixel); font-size: 0.55rem; line-height: 1.9; color: var(--green);
  border: 3px solid var(--green); padding: .6rem; margin-top: 1rem; background: var(--panel);
}}

/* ---------- buttons ---------- */
.stButton > button, .stDownloadButton > button {{
  font-family: var(--body); font-size: 1.35rem;
  background: var(--panel); color: var(--text);
  border: 3px solid var(--grid); border-radius: 0;
  box-shadow: 4px 4px 0 var(--black);
  transition: none; padding: .15rem .6rem;
}}
.stButton > button p {{ font-family: var(--body); font-size: 1.35rem; }}
.stButton > button:hover {{
  border-color: var(--cyan); color: var(--cyan); background: var(--panel);
}}
.stButton > button:active {{ transform: translate(3px, 3px); box-shadow: 1px 1px 0 var(--black); }}
[data-testid="stSidebar"] .stButton > button {{
  justify-content: flex-start; text-align: left; width: 100%;
  box-shadow: none; border-width: 2px; margin-bottom: -.35rem;
}}
button[kind="primary"], button[data-testid="stBaseButton-primary"] {{
  background: var(--yellow) !important; color: var(--bg) !important;
  border-color: var(--yellow) !important;
}}
button[kind="primary"] p, button[data-testid="stBaseButton-primary"] p {{ color: var(--bg) !important; }}
button[kind="primary"]:hover, button[data-testid="stBaseButton-primary"]:hover {{
  background: var(--pink) !important; border-color: var(--pink) !important; color: #fff !important;
}}
.st-key-start button {{ font-family: var(--pixel); padding: .9rem 1rem; box-shadow: 6px 6px 0 var(--pink); }}
.st-key-start button p {{ font-family: var(--pixel); font-size: .85rem; }}

/* ---------- radio (language) ---------- */
[data-testid="stRadio"] label {{ font-family: var(--body); }}

/* ---------- metrics = HUD boxes ---------- */
[data-testid="stMetric"] {{
  background: var(--panel); border: 4px solid var(--cyan); box-shadow: 4px 4px 0 var(--black);
  padding: .7rem .9rem;
}}
[data-testid="stMetricLabel"], [data-testid="stMetricLabel"] p {{
  font-family: var(--body) !important; font-size: 1.25rem !important; color: #b9a9e6 !important;
}}
[data-testid="stMetricValue"], [data-testid="stMetricValue"] div {{
  font-family: var(--pixel) !important; font-size: 1.15rem !important; color: var(--green) !important;
}}

/* ---------- alerts, tabs, tables ---------- */
[data-testid="stAlert"] {{ border-radius: 0; border: 3px solid var(--grid); box-shadow: 4px 4px 0 var(--black); }}
[data-testid="stAlert"] p {{ font-size: 1.4rem; }}
[data-testid="stTabs"] button {{ font-family: var(--pixel); font-size: .6rem; border-radius: 0; }}
[data-testid="stTabs"] button p {{ font-family: var(--pixel); font-size: .6rem; }}
[data-testid="stDataFrame"] {{ border: 3px solid var(--grid); box-shadow: 4px 4px 0 var(--black); }}
[data-testid="stPlotlyChart"] {{
  border: 4px solid var(--grid); background: var(--panel); box-shadow: 4px 4px 0 var(--black); padding: .3rem;
}}
hr {{ border-color: var(--grid) !important; border-top-style: dashed !important; }}

/* ---------- custom components ---------- */
.hero {{
  background: var(--panel); border: 4px solid var(--yellow); box-shadow: 8px 8px 0 var(--pink);
  padding: 1.6rem 1.8rem; margin: 0 0 1.6rem 0; text-align: center;
}}
.hero .tag {{ font-family: var(--pixel); font-size: .6rem; color: var(--cyan); margin-bottom: 1rem; }}
.hero h1 {{ margin: 0 0 1rem 0; font-size: 1.5rem !important; color: var(--yellow) !important; }}
.hero p {{ margin: 0; font-size: 1.6rem; color: var(--text); }}
.blink {{ animation: blink 1s steps(2, start) infinite; }}
@keyframes blink {{ to {{ visibility: hidden; }} }}

.hud {{
  display: flex; justify-content: space-between; align-items: center; gap: 1rem; flex-wrap: wrap;
  font-family: var(--pixel); font-size: .6rem; color: var(--cyan); margin-bottom: .5rem;
}}
.hud b {{ color: var(--yellow); font-weight: normal; }}
.bar {{ display: flex; gap: 3px; margin-bottom: 1.4rem; }}
.bar i {{ flex: 1; height: 14px; background: var(--panel); border: 2px solid var(--grid); }}
.bar i.done {{ background: var(--green); border-color: var(--green); }}
.bar i.now {{ background: var(--yellow); border-color: var(--yellow); animation: blink 1s steps(2, start) infinite; }}

.card {{
  background: var(--panel); border: 4px solid var(--grid); box-shadow: 4px 4px 0 var(--black);
  padding: 1rem 1.2rem; margin-bottom: 1rem;
}}
.card .lbl {{ font-family: var(--pixel); font-size: .55rem; color: var(--cyan); margin-bottom: .6rem; }}
.card .txt {{ font-size: 1.45rem; }}
.big-r {{ font-family: var(--pixel); font-size: 1.6rem; color: var(--green); margin: .5rem 0; text-shadow: 3px 3px 0 var(--black); }}

.decision {{
  font-family: var(--pixel); font-size: .85rem; line-height: 1.6; padding: 1rem 1.2rem; margin: .5rem 0 1rem 0;
  border: 4px solid; box-shadow: 4px 4px 0 var(--black);
}}
.decision.ok {{ color: var(--green); border-color: var(--green); background: #0f2a1c; }}
.decision.warn {{ color: var(--pink); border-color: var(--pink); background: #2e1030; }}

.keyresult {{
  background: var(--panel); border: 4px solid var(--green); box-shadow: 6px 6px 0 var(--black);
  padding: 1rem 1.3rem; margin: 1.2rem 0;
}}
.keyresult .lbl {{ font-family: var(--pixel); font-size: .6rem; color: var(--green); margin-bottom: .6rem; }}
.keyresult .txt {{ font-size: 1.6rem; }}

.worldcard {{
  background: var(--panel); border: 4px solid var(--grid); box-shadow: 4px 4px 0 var(--black);
  padding: .9rem 1rem; height: 100%; min-height: 150px;
}}
.worldcard.here {{ border-color: var(--yellow); }}
.worldcard .w {{ font-family: var(--pixel); font-size: .55rem; color: var(--cyan); margin-bottom: .5rem; }}
.worldcard .n {{ font-family: var(--pixel); font-size: .75rem; color: var(--yellow); margin-bottom: .5rem; line-height: 1.5; }}
.worldcard .d {{ font-size: 1.25rem; line-height: 1.1; color: var(--text); }}

.pixel-ascii {{
  font-family: var(--body); font-size: 1.4rem; color: var(--cyan); background: var(--black);
  border: 3px solid var(--grid); padding: .8rem 1rem; white-space: pre-wrap;
}}

/* ---------- formulas ---------- */
.katex-display {{
  background: var(--panel); border: 3px solid var(--grid); box-shadow: 4px 4px 0 var(--black);
  padding: .8rem 1rem; margin: .2rem 0 .6rem 0; overflow-x: auto; overflow-y: hidden;
}}
.katex {{ color: var(--cyan); font-size: 1.2em; }}
.flabel {{ font-family: var(--pixel); font-size: .6rem; color: var(--green); margin: 1.1rem 0 .5rem 0; line-height: 1.7; }}
.weektag {{
  display: inline-block; font-family: var(--pixel); font-size: .6rem; background: var(--pink); color: #fff;
  padding: .4rem .7rem; border: 3px solid var(--black); box-shadow: 3px 3px 0 var(--black); margin-bottom: .7rem;
}}
.topic {{ font-size: 1.5rem; color: var(--text); margin-bottom: 1rem; }}
.result {{
  background: var(--black); border: 3px solid var(--green); padding: .6rem .9rem; margin: .5rem 0;
  display: flex; justify-content: space-between; align-items: center; gap: 1rem; flex-wrap: wrap;
}}
.result span {{ font-size: 1.35rem; }}
.result b {{ font-family: var(--pixel); font-size: .75rem; color: var(--green); font-weight: normal; }}

/* ---------- forms and inputs ---------- */
[data-testid="stForm"] {{ border: 4px solid var(--grid); border-radius: 0; background: var(--panel); box-shadow: 4px 4px 0 var(--black); }}
[data-testid="stFormSubmitButton"] button {{
  font-family: var(--pixel); background: var(--yellow); color: var(--bg); border: 3px solid var(--yellow);
  border-radius: 0; box-shadow: 4px 4px 0 var(--pink); padding: .6rem 1rem;
}}
[data-testid="stFormSubmitButton"] button p {{ font-family: var(--pixel); font-size: .75rem; color: var(--bg); }}
[data-testid="stFormSubmitButton"] button:hover {{ background: var(--pink); border-color: var(--pink); }}
[data-testid="stFormSubmitButton"] button:hover p {{ color: #fff; }}
[data-baseweb="input"], [data-baseweb="base-input"], [data-baseweb="select"] > div {{ border-radius: 0 !important; }}
input {{ font-family: var(--body) !important; font-size: 1.3rem !important; }}
[data-baseweb="tag"] {{ border-radius: 0 !important; background: var(--pink) !important; }}
[data-testid="stSidebar"] .stButton > button, [data-testid="stSidebar"] .stButton > button p {{ font-size: 1.2rem; }}
</style>
"""


def retro_fig(fig, height=420):
    """Apply the arcade look to a Plotly figure."""
    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor=BLACK,
        font=dict(family="VT323, Courier New, monospace", size=18, color=TEXT),
        title_font=dict(family="Press Start 2P, Courier New, monospace", size=12, color=YELLOW),
        colorway=COLORWAY,
        legend=dict(bgcolor=PANEL, bordercolor=GRID, borderwidth=2, font=dict(size=16)),
        margin=dict(l=50, r=20, t=60, b=50),
        hoverlabel=dict(bgcolor=PANEL, font=dict(family="VT323, monospace", size=16)),
    )
    fig.update_xaxes(gridcolor=GRID, zerolinecolor=GRID, linecolor=TEXT, linewidth=2, mirror=False)
    fig.update_yaxes(gridcolor=GRID, zerolinecolor=GRID, linecolor=TEXT, linewidth=2, mirror=False)
    return fig
