"""FastAPI routes. Numbers come from analysis.py, charts from charts.py.

Run with:  uvicorn app.main:app --reload
"""

from pathlib import Path
from urllib.parse import unquote

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app import analysis, charts

PROJECT_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(
    title="Engineering Branch Trends 2019-2024",
    description="Explore which engineering branches are growing, which are in "
                "demand, and which are declining.",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory=PROJECT_DIR / "static"), name="static")
templates = Jinja2Templates(directory=PROJECT_DIR / "templates")


def page(request, template, **context):
    """Render a template with the values every page needs."""
    df = analysis.load_data()
    first, last = analysis.years(df)
    context.setdefault("branches", analysis.branches(df))
    context.setdefault("period", f"{first}-{last}")
    context.setdefault("active", "")
    return templates.TemplateResponse(request, template, context)


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    """The four answers side by side, over a chart of the whole dataset."""
    charts.cleanup_charts()
    df = analysis.load_data()
    answers = analysis.headline_answers(df)

    chart = charts.growth_vs_demand(analysis.comparison_table(df))
    return page(request, "dashboard.html", active="home", answers=answers, chart=chart)


@app.get("/growth", response_class=HTMLResponse)
def growth(request: Request):
    """Which branches are growing, ranked by percentage change."""
    charts.cleanup_charts()
    df = analysis.load_data()
    table = analysis.growth_table(df)

    return page(
        request, "report.html",
        active="growth",
        title="Which branches are growing?",
        lead="Enrollment at the start and end of the period, ranked by percentage "
             "change so a small branch that grew sharply is not hidden behind a "
             "large one that barely moved.",
        chart=charts.growth_bars(table),
        second_chart=charts.enrollment_trend(
            df, analysis.enrollment_pivot(df),
            highlight=table.iloc[0]["Branch"],
            title="Enrollment over time (fastest grower highlighted)"),
        columns=["Branch", "Start", "End", "Change", "PercentChange"],
        headers=["Branch", "Start", "End", "Change", "Change %"],
        rows=table.to_dict("records"),
        conclusion=analysis.conclusion_for("growth", df),
    )


@app.get("/demand", response_class=HTMLResponse)
def demand(request: Request):
    """Most and least in demand, by average job placement rate."""
    charts.cleanup_charts()
    df = analysis.load_data()
    table = analysis.demand_table(df)

    return page(
        request, "report.html",
        active="demand",
        title="Which branches are most and least in demand?",
        lead="Ranked by the share of graduates placed, not the number of them. A "
             "large branch places more people simply by being large; the rate is "
             "what tells you whether its graduates are wanted.",
        chart=charts.placement_bars(table),
        second_chart=charts.placement_rate_lines(df),
        columns=["Branch", "AveragePlacementRate", "BestYearRate", "WorstYearRate",
                 "AverageStudentsPlaced"],
        headers=["Branch", "Average rate %", "Best year %", "Worst year %",
                 "Avg. students placed"],
        rows=table.to_dict("records"),
        conclusion=analysis.conclusion_for("demand", df),
    )


@app.get("/decline", response_class=HTMLResponse)
def decline(request: Request):
    """Which branches are losing students, and how consistently."""
    charts.cleanup_charts()
    df = analysis.load_data()
    table = analysis.decline_table(df)

    return page(
        request, "report.html",
        active="decline",
        title="Which branches are declining?",
        lead="Counted two ways: how many years in a row enrollment fell, and how "
             "many students were lost in total. They do not agree, and the "
             "difference is the point.",
        chart=charts.decline_bars(table),
        second_chart=charts.enrollment_trend(
            df, analysis.enrollment_pivot(df),
            highlight=table.iloc[0]["Branch"],
            title="Enrollment over time (steepest decline highlighted)"),
        columns=["Branch", "DecliningYears", "TotalChange", "AverageYearlyChange"],
        headers=["Branch", "Years fallen", "Net change", "Average per year"],
        rows=table.to_dict("records"),
        conclusion=analysis.conclusion_for("decline", df),
    )


@app.get("/compare", response_class=HTMLResponse)
def compare(request: Request):
    """Every branch and every headline metric in a single sortable table."""
    charts.cleanup_charts()
    df = analysis.load_data()
    table = analysis.comparison_table(df)

    return page(request, "compare.html", active="compare",
                rows=table.to_dict("records"),
                chart=charts.growth_vs_demand(table),
                answers=analysis.headline_answers(df))


@app.get("/branch/{name}", response_class=HTMLResponse)
def branch(request: Request, name: str):
    """One branch year by year - enrollment, graduates and placement rate."""
    charts.cleanup_charts()
    df = analysis.load_data()

    try:
        rows = analysis.branch_detail(df, unquote(name))
    except ValueError:
        raise HTTPException(status_code=404, detail=f"No branch named {name!r}")

    summary = analysis.comparison_table(df)
    stats = summary[summary["Branch"] == unquote(name)].iloc[0].to_dict()

    return page(request, "branch.html", active="",
                branch=unquote(name),
                chart=charts.branch_history(rows, unquote(name)),
                rows=rows.to_dict("records"),
                stats=stats)
