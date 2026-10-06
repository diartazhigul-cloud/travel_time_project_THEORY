"""Shared storage for data added by players (a plain CSV next to the app)."""
import os
import threading
from datetime import datetime
from pathlib import Path

import pandas as pd

DATA_FILE = Path(__file__).resolve().parent / "player_data.csv"
COLUMNS = ["id", "added", "session", "year", "travel_minutes", "transport_key", "attendance_percent"]
MAX_TOTAL = 2000
_LOCK = threading.Lock()


def _empty():
    return pd.DataFrame(columns=COLUMNS)


def _read():
    if not DATA_FILE.exists():
        return _empty()
    try:
        df = pd.read_csv(DATA_FILE, dtype={"session": str, "transport_key": str})
    except Exception:
        return _empty()
    if any(c not in df.columns for c in COLUMNS):
        return _empty()
    df = df[COLUMNS].copy()
    for c in ["id", "year", "travel_minutes", "attendance_percent"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df = df.dropna(subset=["id", "year", "travel_minutes", "attendance_percent"])
    df = df[(df["travel_minutes"] > 0) & (df["travel_minutes"] <= 600) & df["attendance_percent"].between(0, 100)]
    df["id"] = df["id"].astype(int)
    df["year"] = df["year"].astype(int)
    return df.reset_index(drop=True)


def _write(df):
    tmp = DATA_FILE.with_suffix(".tmp")
    df[COLUMNS].to_csv(tmp, index=False, encoding="utf-8")
    os.replace(tmp, DATA_FILE)


def load_player_data():
    with _LOCK:
        return _read()


def append_row(session, year, travel_minutes, transport_key, attendance_percent):
    """Add one entry. Returns the new id, or None if the storage is full."""
    with _LOCK:
        df = _read()
        if len(df) >= MAX_TOTAL:
            return None
        new_id = int(df["id"].max()) + 1 if len(df) else 1
        row = {
            "id": new_id,
            "added": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "session": session,
            "year": int(year),
            "travel_minutes": round(float(travel_minutes), 2),
            "transport_key": transport_key,
            "attendance_percent": round(float(attendance_percent), 2),
        }
        df = pd.DataFrame([row]) if df.empty else pd.concat([df, pd.DataFrame([row])], ignore_index=True)
        _write(df)
        return new_id


def delete_rows(ids, session):
    """A player can delete only his own entries."""
    with _LOCK:
        df = _read()
        df = df[~(df["id"].isin(list(ids)) & (df["session"] == session))]
        _write(df)


def delete_session(session):
    with _LOCK:
        df = _read()
        _write(df[df["session"] != session])
