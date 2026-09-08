"""What is this written for?

Checking the calculations in analysis.py against the real spreadsheet, without
starting a web server.

The most important test here is test_comparison_table_rows_are_not_scrambled.
An earlier version of comparison_table() built its Branch column from a
positional array while every other column was a pandas Series aligned by index -
so each branch was shown next to another branch's numbers. The page looked
perfectly normal; only the values were wrong. That is the kind of bug worth a
permanent test.

Run with:  pytest
"""

import sys
from pathlib import Path

import pytest

PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_DIR))

from app import analysis  # noqa: E402


@pytest.fixture(scope="module")
def df():
    return analysis.load_data()


# ---------------------------------------------------------------- loading

def test_dataset_loads_with_expected_shape(df):
    assert len(df) == 42                      # 7 branches x 6 years
    assert analysis.years(df) == (2019, 2024)
    assert len(analysis.branches(df)) == 7


def test_no_missing_values(df):
    assert df.isna().sum().sum() == 0


def test_expected_columns_present(df):
    for column in ("Year", "Branch", "Enrollment", "Graduates",
                   "Graduation Rate(%)", "Students Placed", "Job Placement Rate(%)"):
        assert column in df.columns


# ---------------------------------------------------------------- growth

def test_growth_covers_every_branch_once(df):
    table = analysis.growth_table(df)
    assert sorted(table["Branch"]) == analysis.branches(df)


def test_growth_percentage_matches_start_and_end(df):
    for _, row in analysis.growth_table(df).iterrows():
        expected = (row["End"] - row["Start"]) / row["Start"] * 100
        assert row["PercentChange"] == pytest.approx(expected, abs=0.05)


def test_growth_is_sorted_best_first(df):
    values = list(analysis.growth_table(df)["PercentChange"])
    assert values == sorted(values, reverse=True)


# ---------------------------------------------------------------- demand

def test_demand_rates_are_percentages(df):
    table = analysis.demand_table(df)
    assert table["AveragePlacementRate"].between(0, 100).all()
    assert (table["WorstYearRate"] <= table["AveragePlacementRate"]).all()
    assert (table["AveragePlacementRate"] <= table["BestYearRate"]).all()


def test_demand_is_sorted_best_first(df):
    values = list(analysis.demand_table(df)["AveragePlacementRate"])
    assert values == sorted(values, reverse=True)


def test_demand_uses_rate_not_headcount(df):
    """The branch placing the most students is not the one with the best rate.

    This is the distinction the project documentation asks for, and getting it
    wrong would silently turn "most in demand" into "biggest branch".
    """
    table = analysis.demand_table(df)
    best_rate = table.iloc[0]["Branch"]
    most_placed = table.sort_values("AverageStudentsPlaced", ascending=False).iloc[0]["Branch"]
    assert best_rate != most_placed


# ---------------------------------------------------------------- decline

def test_decline_years_within_range(df):
    table = analysis.decline_table(df)
    total = table["TotalYears"].iloc[0]
    assert total == 5                                  # 6 years -> 5 comparisons
    assert table["DecliningYears"].between(0, total).all()


def test_growing_branches_decline_in_fewer_years(df):
    """A branch that grew overall should not also be the most consistent faller."""
    grew = analysis.growth_table(df).iloc[0]["Branch"]
    fell_most = analysis.decline_table(df).iloc[0]["Branch"]
    assert grew != fell_most


# ---------------------------------------------------------------- comparison

def test_comparison_table_rows_are_not_scrambled(df):
    """Every value must belong to the branch named on its own row.

    Regression test: comparison_table() once paired each branch name with
    another branch's figures.
    """
    comparison = analysis.comparison_table(df)
    growth = analysis.growth_table(df).set_index("Branch")
    demand = analysis.demand_table(df).set_index("Branch")
    decline = analysis.decline_table(df).set_index("Branch")

    for _, row in comparison.iterrows():
        branch = row["Branch"]
        assert row["StartEnrollment"] == growth.loc[branch, "Start"]
        assert row["EndEnrollment"] == growth.loc[branch, "End"]
        assert row["PercentChange"] == growth.loc[branch, "PercentChange"]
        assert row["AveragePlacementRate"] == demand.loc[branch, "AveragePlacementRate"]
        assert row["DecliningYears"] == decline.loc[branch, "DecliningYears"]


def test_comparison_matches_raw_spreadsheet(df):
    """Spot-check one branch straight against the source rows."""
    row = analysis.comparison_table(df).set_index("Branch").loc["Computer Science"]
    cs = df[df["Branch"] == "Computer Science"].sort_values("Year")
    assert row["StartEnrollment"] == cs.iloc[0]["Enrollment"]
    assert row["EndEnrollment"] == cs.iloc[-1]["Enrollment"]


# ---------------------------------------------------------------- detail

def test_branch_detail_returns_one_row_per_year(df):
    rows = analysis.branch_detail(df, "Mechanical")
    assert len(rows) == 6
    assert list(rows["Year"]) == [2019, 2020, 2021, 2022, 2023, 2024]
    assert rows.iloc[0]["EnrollmentChange"] == 0        # nothing before the first year


def test_branch_detail_rejects_unknown_branch(df):
    with pytest.raises(ValueError):
        analysis.branch_detail(df, "Astrophysics")


# ---------------------------------------------------------------- headlines

def test_headline_answers_agree_with_the_tables(df):
    answers = analysis.headline_answers(df)
    assert answers["fastest_growing"] == analysis.growth_table(df).iloc[0]["Branch"]
    assert answers["most_demanded"] == analysis.demand_table(df).iloc[0]["Branch"]
    assert answers["least_demanded"] == analysis.demand_table(df).iloc[-1]["Branch"]
    assert answers["most_declining"] == analysis.decline_table(df).iloc[0]["Branch"]


@pytest.mark.parametrize("topic", ["growth", "demand", "decline"])
def test_conclusions_mention_a_real_branch(df, topic):
    text = analysis.conclusion_for(topic, df)
    assert len(text) > 80
    assert any(branch in text for branch in analysis.branches(df))
