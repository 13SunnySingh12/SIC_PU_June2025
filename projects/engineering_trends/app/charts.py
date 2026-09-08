"""What is this written for?

Every chart the site shows. Each function takes the numbers produced by
analysis.py, draws them with matplotlib, saves a PNG into static/charts/ and
returns the filename for the template to render.

Charts are saved under a unique name each time and old ones are cleared on every
request, so a stale image can never be served and the folder cannot grow without
limit.

The colours match the page CSS so the charts look like part of the page rather
than something pasted into it.
"""

import time
import uuid
from pathlib import Path

import matplotlib

# Chosen before pyplot is imported: a web server has no display, and the default
# interactive backend would fail or leak windows.
matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402

CHART_DIR = Path(__file__).resolve().parent.parent / "static" / "charts"

# Charts are kept this long before being swept up, so a page that is still
# loading its images is never left with broken ones.
CHART_MAX_AGE_SECONDS = 600

# Palette shared with static/style.css
INK = "#e8e8ea"
MUTED = "#8b8b94"
PANEL = "#17171b"
GRID = "#2a2a31"
GOOD = "#4ea88a"
BAD = "#c8695f"
NEUTRAL = "#5b6b8c"
ACCENT = "#d7a94b"


def _new_figure(width=10, height=5.2):
    """Create a figure styled to match the page."""
    fig, ax = plt.subplots(figsize=(width, height))
    fig.patch.set_facecolor(PANEL)
    ax.set_facecolor(PANEL)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color(GRID)
    ax.tick_params(colors=MUTED, labelsize=9)
    ax.yaxis.label.set_color(MUTED)
    ax.xaxis.label.set_color(MUTED)
    ax.title.set_color(INK)
    ax.grid(True, color=GRID, linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)
    return fig, ax


def _save(fig):
    """Write the figure to static/charts/ and return just the filename."""
    CHART_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"chart_{uuid.uuid4().hex}.png"
    fig.savefig(CHART_DIR / filename, facecolor=fig.get_facecolor(), dpi=110,
                bbox_inches="tight")
    plt.close(fig)
    return filename


def cleanup_charts(max_age_seconds=CHART_MAX_AGE_SECONDS):
    """Delete charts older than max_age_seconds.

    Deleting *every* chart on each request looks tidier but breaks the page: the
    browser asks for the HTML first and the images a moment later, so a second
    page load in between would wipe the images the first page was still
    fetching. Ageing them out instead keeps the folder from growing while
    leaving recently-served charts readable.
    """
    if not CHART_DIR.exists():
        return
    cutoff = time.time() - max_age_seconds
    for old in CHART_DIR.glob("chart_*.png"):
        try:
            if old.stat().st_mtime < cutoff:
                old.unlink()
        except OSError:
            pass  # being read right now; it will age out on a later request


def _thousands(ax):
    """Show 1280000 as 1,280,000 rather than in scientific notation."""
    ax.get_yaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda v, _: f"{int(v):,}")
    )


# --------------------------------------------------------------------------

def enrollment_trend(df, pivot, highlight=None, title="Enrollment by branch"):
    """Line chart of every branch over time, with one optionally picked out."""
    fig, ax = _new_figure(height=5.6)

    for branch in pivot.columns:
        if branch == highlight:
            ax.plot(pivot.index, pivot[branch], marker="o", linewidth=3,
                    color=ACCENT, label=branch, zorder=3)
        else:
            ax.plot(pivot.index, pivot[branch], marker="o", markersize=4,
                    linewidth=1.4, alpha=0.55, label=branch)

    ax.set_title(title, fontsize=13, pad=14)
    ax.set_xlabel("Year")
    ax.set_ylabel("Students enrolled")
    _thousands(ax)
    legend = ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left", frameon=False,
                       fontsize=9)
    for text in legend.get_texts():
        text.set_color(MUTED)
    return _save(fig)


def growth_bars(growth):
    """Horizontal bars of percentage change - green for growth, red for loss."""
    fig, ax = _new_figure(height=4.8)

    ordered = growth.sort_values("PercentChange")
    colours = [GOOD if v > 0 else BAD for v in ordered["PercentChange"]]
    bars = ax.barh(ordered["Branch"], ordered["PercentChange"], color=colours)

    for bar, value in zip(bars, ordered["PercentChange"]):
        offset = 1.2 if value >= 0 else -1.2
        ax.text(value + offset, bar.get_y() + bar.get_height() / 2,
                f"{value:+.1f}%", va="center",
                ha="left" if value >= 0 else "right",
                color=INK, fontsize=9)

    ax.axvline(0, color=MUTED, linewidth=1)
    ax.set_title("Change in enrollment across the period", fontsize=13, pad=14)
    ax.set_xlabel("Percentage change")
    ax.grid(axis="y", visible=False)
    ax.margins(x=0.16)
    return _save(fig)


def placement_bars(demand):
    """Average placement rate per branch, best and worst picked out."""
    fig, ax = _new_figure(height=4.8)

    ordered = demand.sort_values("AveragePlacementRate")
    colours = [NEUTRAL] * len(ordered)
    colours[-1] = GOOD   # best
    colours[0] = BAD     # worst
    bars = ax.barh(ordered["Branch"], ordered["AveragePlacementRate"], color=colours)

    for bar, value in zip(bars, ordered["AveragePlacementRate"]):
        ax.text(value + 0.6, bar.get_y() + bar.get_height() / 2, f"{value:.1f}%",
                va="center", color=INK, fontsize=9)

    ax.set_title("Average job placement rate", fontsize=13, pad=14)
    ax.set_xlabel("Percent of graduates placed")
    ax.grid(axis="y", visible=False)
    ax.margins(x=0.12)
    return _save(fig)


def placement_rate_lines(df, title="Placement rate year by year"):
    """How each branch's placement rate moved - shows shared market shocks."""
    fig, ax = _new_figure(height=5.2)
    pivot = df.pivot(index="Year", columns="Branch", values="Job Placement Rate(%)")

    for branch in pivot.columns:
        ax.plot(pivot.index, pivot[branch], marker="o", markersize=4, linewidth=1.6,
                alpha=0.85, label=branch)

    ax.set_title(title, fontsize=13, pad=14)
    ax.set_xlabel("Year")
    ax.set_ylabel("Placement rate (%)")
    legend = ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left", frameon=False,
                       fontsize=9)
    for text in legend.get_texts():
        text.set_color(MUTED)
    return _save(fig)


def decline_bars(decline):
    """How many years each branch lost students, out of the years compared."""
    fig, ax = _new_figure(height=4.8)

    ordered = decline.sort_values("DecliningYears")
    total = int(ordered["TotalYears"].iloc[0])
    colours = [BAD if v == total else (ACCENT if v >= total - 1 else NEUTRAL)
               for v in ordered["DecliningYears"]]
    bars = ax.barh(ordered["Branch"], ordered["DecliningYears"], color=colours)

    for bar, value in zip(bars, ordered["DecliningYears"]):
        ax.text(value + 0.06, bar.get_y() + bar.get_height() / 2, f"{int(value)}/{total}",
                va="center", color=INK, fontsize=9)

    ax.set_title(f"Years enrollment fell (out of {total} year-on-year comparisons)",
                 fontsize=13, pad=14)
    ax.set_xlabel("Number of declining years")
    ax.set_xticks(range(total + 1))
    ax.grid(axis="y", visible=False)
    ax.margins(x=0.12)
    return _save(fig)


def growth_vs_demand(comparison):
    """Growth against placement rate - the chart that shows they disagree.

    A branch can be shrinking fast and still place its graduates well, which is
    the single most useful thing a student can take from this data.
    """
    fig, ax = _new_figure(width=9.5, height=5.6)

    x = comparison["PercentChange"]
    y = comparison["AveragePlacementRate"]
    colours = [GOOD if v > 0 else BAD for v in x]

    ax.scatter(x, y, s=150, c=colours, alpha=0.85, edgecolors=INK, linewidths=0.7,
               zorder=3)
    for _, row in comparison.iterrows():
        ax.annotate(row["Branch"],
                    (row["PercentChange"], row["AveragePlacementRate"]),
                    textcoords="offset points", xytext=(0, 13), ha="center",
                    color=INK, fontsize=8.5)

    ax.axvline(0, color=MUTED, linewidth=1, linestyle="--", alpha=0.7)
    ax.axhline(y.mean(), color=MUTED, linewidth=1, linestyle="--", alpha=0.7)
    ax.text(0.6, y.mean() + 0.12, "average placement rate", color=MUTED, fontsize=8)

    ax.set_title("Growing branches are not always the ones that place best",
                 fontsize=13, pad=16)
    ax.set_xlabel("Enrollment change (%)")
    ax.set_ylabel("Average placement rate (%)")
    ax.margins(x=0.18, y=0.22)
    return _save(fig)


def branch_history(rows, branch):
    """Two stacked panels for one branch: enrollment, then placement rate."""
    fig, (top, bottom) = plt.subplots(2, 1, figsize=(10, 6.4), sharex=True)
    fig.patch.set_facecolor(PANEL)

    for ax in (top, bottom):
        ax.set_facecolor(PANEL)
        for spine in ("top", "right"):
            ax.spines[spine].set_visible(False)
        for spine in ("left", "bottom"):
            ax.spines[spine].set_color(GRID)
        ax.tick_params(colors=MUTED, labelsize=9)
        ax.yaxis.label.set_color(MUTED)
        ax.xaxis.label.set_color(MUTED)
        ax.grid(True, color=GRID, linewidth=0.6, alpha=0.7)
        ax.set_axisbelow(True)

    top.plot(rows["Year"], rows["Enrollment"], marker="o", linewidth=2.4, color=ACCENT)
    top.fill_between(rows["Year"], rows["Enrollment"], color=ACCENT, alpha=0.12)
    top.set_ylabel("Enrolled")
    top.set_title(f"{branch}", fontsize=13, color=INK, pad=14)
    _thousands(top)

    colours = [GOOD if v >= 75 else BAD for v in rows["Job Placement Rate(%)"]]
    bottom.bar(rows["Year"], rows["Job Placement Rate(%)"], color=colours, width=0.55)
    for year, rate in zip(rows["Year"], rows["Job Placement Rate(%)"]):
        bottom.text(year, rate + 1.2, f"{rate:.0f}%", ha="center", color=MUTED,
                    fontsize=8.5)
    bottom.set_ylabel("Placed (%)")
    bottom.set_xlabel("Year")
    bottom.set_ylim(0, 105)

    fig.tight_layout()
    return _save(fig)
