import re

import numpy as np
import pandas as pd

from data import RAW_ROWS

HOUR_WORDS = ("сағат", "сагат", "час", "часа", "hour", "hours")
YEAR_WORDS = ("жыл", "year", "год")
PLANE_WORDS = ("самолет", "самолёт", "plane", "airplane", "aircraft")


def _nums(text):
    return [float(x.replace(",", ".")) for x in re.findall(r"\d+(?:[.,]\d+)?", text)]


def parse_minutes(value):
    s = str(value).strip().lower().replace("–", "-").replace("—", "-")
    if any(w in s for w in YEAR_WORDS):
        return np.nan, "Invalid: year entered instead of minutes"

    nums = _nums(s)
    is_hour = any(w in s for w in HOUR_WORDS) or s in ("час", "часа")

    if is_hour:
        if not nums:
            return 60.0, "1 hour interpreted as 60 minutes"
        hours = nums[0]
        if len(nums) >= 2:
            hours = (nums[0] + nums[1]) / 2
        return hours * 60.0, f"{hours:g} hour(s) converted to minutes"

    if len(nums) >= 2:
        return (nums[0] + nums[1]) / 2.0, "Range converted to midpoint"
    if len(nums) == 1:
        return nums[0], "Numeric value interpreted as minutes"
    return np.nan, "Could not parse travel time"


def parse_attendance(value):
    s = str(value).strip().lower().replace("%", "").replace("–", "-").replace("—", "-")
    nums = _nums(s)
    if len(nums) >= 2:
        return (nums[0] + nums[1]) / 2.0, "Attendance range converted to midpoint"
    if len(nums) == 1:
        return nums[0], "Numeric percent"
    return np.nan, "Could not parse attendance"


def transport_key(raw):
    t = str(raw).lower()
    if any(w in t for w in PLANE_WORDS):
        return "plane"
    if ("пешком" in t and "автобус" in t) or ("walk" in t and "bus" in t):
        return "walk_bus"
    if "жаяу" in t or "foot" in t or "пешком" in t:
        return "walk"
    if "такси" in t or "жеке көлік" in t or "личное" in t or "car" in t:
        return "car"
    if "автобус" in t or "bus" in t or "қоғамдық" in t:
        return "bus"
    return "other"


def travel_bin(minutes):
    if pd.isna(minutes):
        return None
    if minutes <= 15:
        return "0–15"
    if minutes <= 30:
        return "16–30"
    if minutes <= 60:
        return "31–60"
    return "61+"


def build_tables():
    df = pd.DataFrame(RAW_ROWS)
    travel = df["travel_raw"].apply(parse_minutes)
    att = df["attendance_raw"].apply(parse_attendance)
    df["travel_minutes"] = travel.apply(lambda x: x[0])
    df["travel_note"] = travel.apply(lambda x: x[1])
    df["attendance_percent"] = att.apply(lambda x: x[0])
    df["attendance_note"] = att.apply(lambda x: x[1])
    df["transport_key"] = df["transport_raw"].apply(transport_key)
    df["travel_bin"] = df["travel_minutes"].apply(travel_bin)

    reasons = []
    keep = []
    for _, row in df.iterrows():
        if row["transport_key"] == "plane":
            reasons.append("Excluded: plane / unrealistic commute")
            keep.append(False)
        elif pd.isna(row["travel_minutes"]):
            reasons.append("Excluded: invalid travel time")
            keep.append(False)
        elif pd.isna(row["attendance_percent"]):
            reasons.append("Excluded: invalid attendance")
            keep.append(False)
        else:
            reasons.append("Kept for analysis")
            keep.append(True)
    df["action"] = reasons
    df["keep"] = keep
    df["travel_bin"] = df["travel_minutes"].apply(travel_bin)

    analysis = df.loc[df["keep"]].copy()
    return df, analysis
