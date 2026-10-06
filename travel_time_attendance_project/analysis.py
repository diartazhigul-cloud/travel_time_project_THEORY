"""Statistics helpers used by the main analysis and by the sandbox page."""
import numpy as np
from scipy import stats

ALPHA = 0.05


def summarize(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    return {
        "mean": series.mean(),
        "median": series.median(),
        "min": series.min(),
        "max": series.max(),
        "std": series.std(ddof=1),
        "var": series.var(ddof=1),
        "q1": q1,
        "q3": q3,
        "iqr": q3 - q1,
    }


def fisher_ci(r, n):
    if n <= 3 or abs(r) >= 1:
        return (np.nan, np.nan)
    z = np.arctanh(r)
    se = 1.0 / np.sqrt(n - 3)
    return float(np.tanh(z - 1.96 * se)), float(np.tanh(z + 1.96 * se))


def analyze(x, y):
    """Pearson r, p-value, regression and CI. Returns None if it cannot be calculated."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = len(x)
    if n < 3 or np.ptp(x) == 0 or np.ptp(y) == 0:
        return None
    r, p = stats.pearsonr(x, y)
    reg = stats.linregress(x, y)
    lo, hi = fisher_ci(r, n)
    return {
        "n": n,
        "r": float(r),
        "p": float(p),
        "slope": float(reg.slope),
        "intercept": float(reg.intercept),
        "r2": float(reg.rvalue ** 2),
        "ci_lo": lo,
        "ci_hi": hi,
        "df": n - 2,
        "t": float(r * np.sqrt((n - 2) / (1 - r ** 2))) if abs(r) < 1 else float("inf"),
        "reject": bool(p < ALPHA),
    }
