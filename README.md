# SIC_PU_June2025

Work from the **Samsung Innovation Campus** *Coding & Programming in Python*
programme (June 2025): Python fundamentals, data structures and algorithms, data
analytics, database connectivity, and problem solving — plus the hackathon
project built at the end of it.

## Layout

```
SIC_PU_June2025/
├── projects/
│   └── engineering_branch_analysis/   FastAPI web app - the hackathon project
├── coursework/
│   ├── 01_python_basics/              conditionals, patterns, number problems,
│   │                                  lists, recursion, list-backed stack & queue
│   ├── 02_dsa/                        linked lists, searching, sorting, BST & AVL
│   ├── 03_data_analytics/             numpy, pandas, matplotlib, lambdas, regex
│   └── 04_databases_and_apis/         MySQL CRUD, a REST API, an API client
├── problem_solving/                   standalone algorithm problems
└── docs/                              written answers and the git assignment
```

Every file opens with a short comment saying what it is written for.

## The main project

**[Engineering Branch Analysis](projects/engineering_branch_analysis/)** — a
FastAPI web app that analyses B.Tech enrolment and placement data for seven
engineering branches over 2019–2024. Four report pages, each rendering a
matplotlib/seaborn chart plus a written conclusion, with the analysis kept
separate from the web layer. Covered by end-to-end tests.

```bash
cd projects/engineering_branch_analysis
pip install -r requirements.txt
uvicorn app.main:app --reload --port 5762
```

## Coursework highlights

| Area | What is in there |
|---|---|
| `01_python_basics` | Control flow, pattern printing, digit and series problems, an income-tax calculator, stacks and queues on plain lists |
| `02_dsa` | Stack and queue on singly and doubly linked lists; binary and recursive search; bubble, insertion, merge, quick and selection sort; BST and AVL trees with console menus |
| `03_data_analytics` | numpy array creation, reshaping, broadcasting and matrix maths; pandas CSV loading and row iteration; eight matplotlib chart types; lambdas with `map`/`filter`/`reduce`/`sort`; regex extraction and substitution |
| `04_databases_and_apis` | Employee CRUD over MySQL with `pymysql`; a **FastAPI** REST API over a `persons` table, with tests; an OpenWeatherMap client |

`problem_solving/` holds standalone problems — stacks, greedy, arrays and
strings, plus a `trees/` folder with BST and AVL problems and N-Queens.

## Running things

Most files under `coursework/` and `problem_solving/` are self-contained console
scripts — run any of them directly:

```bash
python coursework/02_dsa/sorting/merge_sort.py
```

The two web projects have their own entry points and are run with `uvicorn`.

## Setup

Everything installs into a project-local virtual environment, so this repo never
touches your global Python:

```bash
python -m venv .venv
```

Activate it — PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

Git Bash / macOS / Linux:

```bash
source .venv/bin/activate
```

Then install:

```bash
pip install -r requirements.txt
```

Your prompt shows `(.venv)` once it is active. `deactivate` leaves it. `.venv/`
is gitignored, so each machine builds its own.

> If PowerShell blocks the activation script, allow local scripts for your user
> once with `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, or skip
> activation and call `.venv\Scripts\python.exe` directly.

Nothing is hardcoded. The MySQL projects and the weather client read their
credentials from a `.env` file, falling back to real environment variables
(which take precedence if both are set):

```bash
cp coursework/04_databases_and_apis/.env.example coursework/04_databases_and_apis/.env
```

Fill in the real values there. `.env` is gitignored; `.env.example` is the
template showing which keys are needed.

## Tests

```bash
pytest projects/engineering_branch_analysis
```
