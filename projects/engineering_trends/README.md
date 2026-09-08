# Engineering Branch Trends (2019–2024)

A web application that turns six years of B.Tech enrollment and placement data
into answers about which engineering branches are growing, which are in demand,
and which are declining.

Built for the Samsung Innovation Campus programme, using only the tools covered
in the course: **Python, pandas, NumPy, Matplotlib, FastAPI and Jinja2**.

## The question it answers

> How can real-world engineering enrollment and placement data from 2019 to 2024
> be turned into an intuitive, visual, and analytical web platform that lets
> students, educators, institutions, and policymakers explore which engineering
> branches are growing, which are most and least in demand, and which are
> declining?

## Pages

| Page | Question it answers |
|---|---|
| `/` | All four answers at a glance, plus growth against demand |
| `/growth` | Which branches are growing, ranked by percentage change |
| `/demand` | Which are most and least in demand, by placement rate |
| `/decline` | Which are losing students, and how consistently |
| `/compare` | Every branch and metric in one table |
| `/branch/{name}` | One branch year by year |

## What the data shows

| Finding | Branch | Figure |
|---|---|---|
| Growing fastest | Computer Science | **+36.9%** enrollment |
| Most in demand | Information Technology | **81.2%** placed |
| Least in demand | Civil | **74.4%** placed |
| Declining most consistently | Mechanical | fell in **5 of 5** years |

The most interesting result is that these disagree. Information Technology has
the **best** placement record of any branch while losing **39.2%** of its
students — the steepest decline in the dataset. Student preference has shifted
far more sharply than employer demand has, which is exactly the kind of thing a
table of raw numbers hides and a chart makes obvious.

### A note on how "demand" is measured

Demand is calculated from **Job Placement Rate (%)**, not the raw number of
students placed. A large branch places more people simply by being large;
ranking on headcount would just re-rank the branches by size. The rate answers
the question actually being asked — what share of a branch's graduates found
work.

## Layout

```
engineering_trends/
├── app/
│   ├── analysis.py    pandas + NumPy: every calculation, no charts, no web
│   ├── charts.py      Matplotlib: every figure, saved as PNG
│   └── main.py        FastAPI: one route per question
├── data/              the source spreadsheet (read-only)
├── templates/         Jinja2 - base layout plus one template per page type
├── static/            style.css, and charts/ generated at request time
├── tests/             37 tests over the calculations and the pages
└── docs/              the original project report
```

The split is deliberate: `analysis.py` returns numbers and nothing else, so every
figure on the site can be tested without starting a server. If a number appears
on a page, it came from there.

## Running it

```bash
pip install -r requirements.txt
```

```bash
uvicorn app.main:app --reload
```

Open <http://127.0.0.1:8000>.

## Tests

```bash
pytest
```

37 tests: the calculations against the spreadsheet, and every page against the
running app. Two are worth calling out —

- `test_comparison_table_rows_are_not_scrambled` — an earlier version built the
  branch column from a positional array while the other columns were pandas
  Series aligned by index, so each branch was shown beside **another branch's**
  figures. The page looked perfectly normal. Only the values were wrong.
- `test_page_charts_are_actually_served` — fetches every chart a page references,
  because a page with a broken image still returns `200`.

## Technology

| Used | Where it comes from |
|---|---|
| Python 3.12 | throughout the course |
| pandas | `coursework/03_data_analytics/pandas` |
| NumPy | `coursework/03_data_analytics/numpy` |
| Matplotlib | `coursework/03_data_analytics/matplotlib` |
| FastAPI + Jinja2 | `coursework/04_databases_and_apis/person_api` |
| pytest | used across the repository |
| openpyxl | required for pandas to read `.xlsx` |

No JavaScript, no CSS framework, no database — the dataset is the source of
truth and is read fresh on every request.
