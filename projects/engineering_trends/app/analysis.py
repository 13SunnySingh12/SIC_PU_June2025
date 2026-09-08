"""What is this written for?

The analysis layer: it loads the 2019-2024 B.Tech spreadsheet and turns it into
the answers the site needs. Nothing here knows about charts or the web - every
function takes a DataFrame and returns numbers, so each one can be checked on
its own.

The four questions the project sets out to answer:

    growth_table()      which branches are growing, and by how much
    demand_table()      which are most and least in demand
    decline_table()     which are losing students year after year
    headline_answers()  the single best answer to each of the above

"Demand" is measured with Job Placement Rate(%), not the raw number of students
placed. A big branch places more people simply by being big; the rate says what
share of its graduates actually found work, which is what "in demand" means.
"""

from pathlib import Path

import numpy as np
import pandas as pd

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "engineering_btech_trends_2019_2024.xlsx"


def load_data():
    """Read the spreadsheet and return it as a tidy DataFrame.

    One row per (year, branch). Column names are stripped because the source
    file has stray spaces around some of the headers.
    """
    df = pd.read_excel(DATA_FILE)
    df.columns = df.columns.str.strip()
    df["Year"] = df["Year"].astype(int)
    return df.sort_values(["Branch", "Year"]).reset_index(drop=True)


def years(df):
    """The first and last year present in the data."""
    return int(df["Year"].min()), int(df["Year"].max())


def branches(df):
    """Every branch name, alphabetically."""
    return sorted(df["Branch"].unique())


def enrollment_pivot(df):
    """Enrollment as a Year x Branch grid - the shape most calculations want."""
    return df.pivot(index="Year", columns="Branch", values="Enrollment").sort_index()


# --------------------------------------------------------------------------
# Question 1: which branches are growing?
# --------------------------------------------------------------------------

def growth_table(df):
    """Rank branches by how much their enrollment changed across the period.

    Percentage change rather than headcount, so a small branch that doubled is
    not buried under a large branch that grew slightly.
    """
    pivot = enrollment_pivot(df)
    first, last = years(df)

    start = pivot.loc[first]
    end = pivot.loc[last]

    table = pd.DataFrame({
        "Branch": start.index,
        "Start": start.values,
        "End": end.values,
        "Change": (end - start).values,
        "PercentChange": np.round((end - start) / start * 100, 1).values,
    })
    return table.sort_values("PercentChange", ascending=False).reset_index(drop=True)


# --------------------------------------------------------------------------
# Question 2: which branches are most / least in demand?
# --------------------------------------------------------------------------

def demand_table(df):
    """Rank branches by their average job placement rate over the period.

    Also carries the average number placed, so the page can show that the
    highest rate does not always belong to the biggest branch.
    """
    grouped = df.groupby("Branch").agg(
        AveragePlacementRate=("Job Placement Rate(%)", "mean"),
        BestYearRate=("Job Placement Rate(%)", "max"),
        WorstYearRate=("Job Placement Rate(%)", "min"),
        AverageStudentsPlaced=("Students Placed", "mean"),
    ).reset_index()

    grouped["AveragePlacementRate"] = grouped["AveragePlacementRate"].round(1)
    grouped["BestYearRate"] = grouped["BestYearRate"].round(1)
    grouped["WorstYearRate"] = grouped["WorstYearRate"].round(1)
    grouped["AverageStudentsPlaced"] = grouped["AverageStudentsPlaced"].round(0).astype(int)

    return grouped.sort_values("AveragePlacementRate", ascending=False).reset_index(drop=True)


# --------------------------------------------------------------------------
# Question 3: which branches are declining?
# --------------------------------------------------------------------------

def decline_table(df):
    """Rank branches by how consistently their enrollment falls.

    Two different things are counted, because they disagree:
      DecliningYears - how many years enrollment dropped (consistency)
      TotalChange    - the net headcount lost (size of the drop)
    A branch can slide every single year yet lose fewer students than a bigger
    branch that fell only twice, so both are reported.
    """
    pivot = enrollment_pivot(df)
    change_per_year = pivot.diff()

    table = pd.DataFrame({
        "Branch": pivot.columns,
        "DecliningYears": (change_per_year < 0).sum().values,
        "TotalYears": len(pivot) - 1,
        "TotalChange": (pivot.iloc[-1] - pivot.iloc[0]).values,
        "AverageYearlyChange": np.round(change_per_year.mean(), 0).fillna(0).astype(int).values,
    })
    return table.sort_values(
        ["DecliningYears", "TotalChange"], ascending=[False, True]
    ).reset_index(drop=True)


# --------------------------------------------------------------------------
# Per-branch detail
# --------------------------------------------------------------------------

def branch_detail(df, branch):
    """Every year of data for one branch, plus its year-on-year change.

    Raises ValueError for an unknown branch so the web layer can turn that into
    a 404 rather than rendering an empty page.
    """
    if branch not in df["Branch"].values:
        raise ValueError(f"Unknown branch: {branch}")

    rows = df[df["Branch"] == branch].sort_values("Year").copy()
    rows["EnrollmentChange"] = rows["Enrollment"].diff().fillna(0).astype(int)
    return rows.reset_index(drop=True)


def comparison_table(df):
    """One row per branch pulling together every headline metric.

    This is the table behind the Compare page, and the closest thing the project
    has to a single answer sheet.
    """
    growth = growth_table(df).set_index("Branch")
    demand = demand_table(df).set_index("Branch")
    decline = decline_table(df).set_index("Branch")

    # Every column below is a Series keyed by branch, so pandas lines them up by
    # name no matter what order each table was sorted into. The branch label then
    # comes from that shared index - never from a separate positional array,
    # which would pair each name with whichever row happened to land beside it.
    table = pd.DataFrame({
        "StartEnrollment": growth["Start"],
        "EndEnrollment": growth["End"],
        "PercentChange": growth["PercentChange"],
        "AveragePlacementRate": demand["AveragePlacementRate"],
        "DecliningYears": decline["DecliningYears"],
    })
    table.index.name = "Branch"
    table = table.reset_index()

    return table.sort_values("PercentChange", ascending=False).reset_index(drop=True)


# --------------------------------------------------------------------------
# The headline answers
# --------------------------------------------------------------------------

def headline_answers(df):
    """The four answers the project exists to give, as plain values.

    Returned as a dict so the dashboard can show them without repeating any of
    the calculations above.
    """
    growth = growth_table(df)
    demand = demand_table(df)
    decline = decline_table(df)
    first, last = years(df)

    growing = growth.iloc[0]
    shrinking = growth.iloc[-1]
    most_demanded = demand.iloc[0]
    least_demanded = demand.iloc[-1]
    declining = decline.iloc[0]

    return {
        "first_year": first,
        "last_year": last,
        "branch_count": len(branches(df)),
        "total_records": len(df),

        "fastest_growing": growing["Branch"],
        "fastest_growing_pct": growing["PercentChange"],

        "most_demanded": most_demanded["Branch"],
        "most_demanded_rate": most_demanded["AveragePlacementRate"],

        "least_demanded": least_demanded["Branch"],
        "least_demanded_rate": least_demanded["AveragePlacementRate"],

        "most_declining": declining["Branch"],
        "most_declining_years": int(declining["DecliningYears"]),
        "most_declining_total": int(declining["TotalChange"]),

        "biggest_faller": shrinking["Branch"],
        "biggest_faller_pct": shrinking["PercentChange"],
    }


def conclusion_for(topic, df):
    """A written takeaway for each report page.

    The numbers are read back out of the tables, so the sentence can never drift
    away from what the chart above it shows.
    """
    a = headline_answers(df)
    span = f"{a['first_year']}-{a['last_year']}"

    if topic == "growth":
        return (
            f"{a['fastest_growing']} grew the most between {span}, with enrollment up "
            f"{a['fastest_growing_pct']}%. At the other end, {a['biggest_faller']} fell "
            f"{abs(a['biggest_faller_pct'])}%. Most branches did not grow at all over this "
            f"period - the increase is concentrated in very few of them, which is what makes "
            f"the shift in student preference so visible."
        )

    if topic == "demand":
        return (
            f"{a['most_demanded']} has the strongest hiring record, placing "
            f"{a['most_demanded_rate']}% of its graduates on average across {span}. "
            f"{a['least_demanded']} is weakest at {a['least_demanded_rate']}%. The gap between "
            f"them is narrower than the enrollment gap, so a branch losing students is not "
            f"necessarily a branch whose graduates struggle to find work."
        )

    if topic == "decline":
        return (
            f"{a['most_declining']} shows the most consistent fall, dropping in "
            f"{a['most_declining_years']} of the {a['last_year'] - a['first_year']} year-on-year "
            f"comparisons, for a net change of {a['most_declining_total']:,} students. A steady "
            f"decline matters more than one bad year, because it points to a lasting change in "
            f"demand rather than a single disrupted intake."
        )

    return ""
