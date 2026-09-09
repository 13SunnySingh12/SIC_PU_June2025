"""Tests that every page renders, serves its chart, and shows the right figures."""

import html as html_module
import re
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_DIR))

from app import analysis  # noqa: E402
from app.main import app  # noqa: E402

CHART_PATTERN = r"/static/charts/chart_[0-9a-f]+\.png"


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="module")
def df():
    return analysis.load_data()


def charts_in(html):
    return sorted(set(re.findall(CHART_PATTERN, html)))


def as_rendered(branch):
    """Branch names reach the page HTML-escaped - "A & B" becomes "A &amp; B"."""
    return html_module.escape(branch)


# ---------------------------------------------------------------- pages

@pytest.mark.parametrize("path", ["/", "/growth", "/demand", "/decline", "/compare"])
def test_page_renders(client, path):
    response = client.get(path)
    assert response.status_code == 200
    assert "Engineering Branch Trends" in response.text


@pytest.mark.parametrize("path", ["/", "/growth", "/demand", "/decline", "/compare"])
def test_page_charts_are_actually_served(client, path):
    """The images a page references must exist and be fetchable."""
    html = client.get(path).text
    images = charts_in(html)
    assert images, f"{path} rendered no chart"
    for image in images:
        assert client.get(image).status_code == 200


def test_navigation_links_to_every_report(client):
    html = client.get("/").text
    for path in ("/growth", "/demand", "/decline", "/compare"):
        assert f'href="{path}"' in html or path in html


def test_stylesheet_is_served(client):
    response = client.get("/static/style.css")
    assert response.status_code == 200
    assert "--accent" in response.text


# ---------------------------------------------------------------- content

def test_dashboard_shows_the_four_answers(client, df):
    html = client.get("/").text
    answers = analysis.headline_answers(df)
    for key in ("fastest_growing", "most_demanded", "least_demanded", "most_declining"):
        assert as_rendered(answers[key]) in html


def test_growth_page_lists_every_branch(client, df):
    html = client.get("/growth").text
    for branch in analysis.branches(df):
        assert as_rendered(branch) in html


def test_compare_page_pairs_each_branch_with_its_own_numbers(client, df):
    """Guards the row-scrambling bug at the HTML level, not just in pandas."""
    html = client.get("/compare").text
    for _, row in analysis.comparison_table(df).iterrows():
        # the branch name and its end-of-period enrollment must appear together
        formatted = f"{int(row['EndEnrollment']):,}"
        position_branch = html.find(as_rendered(row["Branch"]))
        position_value = html.find(formatted, position_branch)
        assert position_branch != -1, f"{row['Branch']} missing from the page"
        assert position_value != -1, f"{row['Branch']} is not followed by {formatted}"
        assert position_value - position_branch < 400, \
            f"{row['Branch']} is not next to its own figure {formatted}"


# ---------------------------------------------------------------- branches

def test_every_branch_has_a_working_page(client, df):
    for branch in analysis.branches(df):
        response = client.get(f"/branch/{branch}")
        assert response.status_code == 200
        assert as_rendered(branch) in response.text


def test_branch_page_shows_all_six_years(client):
    html = client.get("/branch/Mechanical").text
    for year in range(2019, 2025):
        assert str(year) in html


def test_unknown_branch_is_404(client):
    assert client.get("/branch/Astrophysics").status_code == 404
