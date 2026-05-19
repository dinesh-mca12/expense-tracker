# Expense Tracker Project Submission

This file contains the complete project summary, commands, folder structure,
source files, Git history, Git commands, GitHub workflow steps, pull request
text, and sample issue details for the Flask Expense Tracker application.

## Project Overview

Expense Tracker is a simple responsive web application built with Python Flask.
It stores expense data locally in SQLite and supports:

- Add Expense
- View Expenses
- Delete Expense
- Expense Title
- Amount
- Date
- Category

Supported categories:

- Food
- Travel
- Utilities
- Needs
- Wants
- Savings

## Local App URL

```text
http://127.0.0.1:5000
```

## Verification Performed

```powershell
python -m pip install -r requirements.txt
python -m compileall .
Invoke-WebRequest -Uri http://127.0.0.1:5000 -UseBasicParsing
Invoke-WebRequest -Uri http://127.0.0.1:5000/add -UseBasicParsing
```

Flask smoke test performed:

- Opened home page.
- Added a sample expense.
- Verified the expense appeared in the list.
- Deleted the sample expense.
- Verified the expense was removed from SQLite.

## GitHub Status Note

GitHub repository creation and push could not be completed automatically in this
environment because:

- `gh` GitHub CLI is not installed.
- `GITHUB_TOKEN` is not set.
- `GH_TOKEN` is not set.
- The available GitHub connector can create issues, PRs, files, and branches in
  existing repositories, but does not expose repository creation or local git
  push.

Use the GitHub workflow commands below after installing and authenticating
GitHub CLI.

## Terminal Commands Used

```powershell
New-Item -ItemType Directory -Force -Path .\expense-tracker, .\expense-tracker\templates, .\expense-tracker\static, .\expense-tracker\data

git --version
gh --version
python --version

git init -b main
git status -sb
git config user.name
git config user.email
git add .
git commit -m "Initial project setup"

git checkout -b feature-expense-list
git diff --stat
git status -sb
git add README.md app.py static/styles.css templates/base.html templates/index.html
git commit -m "Added expense list feature"

git checkout -b feature-add-expense
git diff --stat
git status -sb
git add README.md app.py static/styles.css templates/base.html templates/index.html templates/add_expense.html
git commit -m "Implemented add expense feature"

git checkout main
git merge --no-ff feature-expense-list -m "Merge feature-expense-list into main"
git merge --no-ff feature-add-expense -m "Merge feature-add-expense into main"
git log --oneline --graph

git checkout -b improve-delete-feature
git diff --stat
git status -sb
git add README.md app.py static/styles.css templates/index.html
git commit -m "Added delete expense improvement"

python -m pip show Flask
python -m pip install -r requirements.txt
python -m compileall .

git checkout main
git add app.py
git commit -m "Fix Flask import"
git checkout improve-delete-feature
git rebase main

git log --oneline --graph
git log --oneline --graph --all --decorate
git status -sb

Get-NetTCPConnection -LocalPort 5000 -ErrorAction SilentlyContinue
Start-Process -FilePath python -ArgumentList '-m','flask','--app','app','run','--host','127.0.0.1','--port','5000' -WorkingDirectory 'D:\expense_tracker\expense-tracker' -WindowStyle Hidden -PassThru
Invoke-WebRequest -Uri http://127.0.0.1:5000 -UseBasicParsing
Invoke-WebRequest -Uri http://127.0.0.1:5000/add -UseBasicParsing
```

## Final Folder Structure

```text
expense-tracker/
  .gitignore
  README.md
  PROJECT_SUBMISSION.md
  app.py
  requirements.txt
  data/
    .gitkeep
  static/
    styles.css
  templates/
    add_expense.html
    base.html
    index.html
```

Runtime SQLite database:

```text
data/expenses.db
```

The database file is generated automatically and ignored by Git.

## Git History

```text
* b2a33ac Added delete expense improvement
* d1e211c Fix Flask import
*   b653d25 Merge feature-add-expense into main
|\  
| * a1551ad Implemented add expense feature
* | 3337f37 Merge feature-expense-list into main
|\| 
| * fb9b733 Added expense list feature
|/  
* 8b35113 Initial project setup
```

## Git Commands Separately

```powershell
git init -b main
git add .
git commit -m "Initial project setup"

git checkout -b feature-expense-list
git add README.md app.py static/styles.css templates/base.html templates/index.html
git commit -m "Added expense list feature"

git checkout -b feature-add-expense
git add README.md app.py static/styles.css templates/base.html templates/index.html templates/add_expense.html
git commit -m "Implemented add expense feature"

git checkout main
git merge --no-ff feature-expense-list -m "Merge feature-expense-list into main"
git merge --no-ff feature-add-expense -m "Merge feature-add-expense into main"
git log --oneline --graph

git checkout -b improve-delete-feature
git add README.md app.py static/styles.css templates/index.html
git commit -m "Added delete expense improvement"

git checkout main
git add app.py
git commit -m "Fix Flask import"

git checkout improve-delete-feature
git rebase main
git log --oneline --graph --all --decorate
```

## GitHub Workflow Steps

Run these commands after installing GitHub CLI and logging in:

```powershell
gh auth login

gh repo create expense-tracker --public --source=. --remote=origin --push

git push --all origin
git push --tags origin

gh pr create --base main --head improve-delete-feature --title "Added delete expense improvement" --body-file PULL_REQUEST.md

gh label create enhancement --color a2eeef --description "New feature or request" --force

gh issue create --title "Improve expense category filtering" --body "Add dropdown filter to view expenses category-wise" --label enhancement
```

## Pull Request Title And Description

Title:

```text
Added delete expense improvement
```

Description:

```markdown
Adds a POST-based delete action for saved expenses.

Changes:
- Adds `/delete/<expense_id>` route.
- Adds delete buttons to the expense table.
- Shows success/error flash messages.
- Updates README with delete feature details.

Validation:
- Ran Python compile check.
- Ran Flask smoke test for add, list, and delete flow.
```

## Sample GitHub Issue

Title:

```text
Improve expense category filtering
```

Description:

```text
Add dropdown filter to view expenses category-wise
```

Label:

```text
enhancement
```

## Complete Project Files

### `.gitignore`

```gitignore
__pycache__/
*.py[cod]
.pytest_cache/
.venv/
venv/
env/
.env
instance/
data/*.db
data/*.sqlite
*.log
```

### `requirements.txt`

```text
Flask>=3.0,<4.0
```

### `README.md`

````markdown
# Expense Tracker

A simple responsive Expense Tracker web application built with Python Flask.

The app will use local SQLite storage and support:

- Adding expenses
- Viewing expenses
- Deleting expenses
- Categories for Food, Travel, Utilities, Needs, Wants, and Savings

## Expense List

The home page displays all saved expenses in newest-first order with the title,
category, date, amount, and a total spending summary.

## Add Expense

Use the `Add Expense` page to save a title, amount, date, and one of the
supported categories to the local SQLite database.

## Delete Expense

Each saved row includes a delete action that removes the expense from local
SQLite storage and returns to the updated expense list.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in your browser.
````

### `app.py`

```python
import sqlite3
from datetime import date
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, url_for


app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-expense-tracker-secret"

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATABASE = DATA_DIR / "expenses.db"

CATEGORIES = [
    "Food",
    "Travel",
    "Utilities",
    "Needs",
    "Wants",
    "Savings",
]


def get_connection():
    DATA_DIR.mkdir(exist_ok=True)
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                amount REAL NOT NULL,
                expense_date TEXT NOT NULL,
                category TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


def get_expenses():
    init_db()
    with get_connection() as connection:
        return connection.execute(
            """
            SELECT id, title, amount, expense_date, category
            FROM expenses
            ORDER BY expense_date DESC, id DESC
            """
        ).fetchall()


def create_expense(title, amount, expense_date, category):
    init_db()
    with get_connection() as connection:
        connection.execute(
            """
            INSERT INTO expenses (title, amount, expense_date, category)
            VALUES (?, ?, ?, ?)
            """,
            (title, amount, expense_date, category),
        )


def remove_expense(expense_id):
    init_db()
    with get_connection() as connection:
        cursor = connection.execute(
            "DELETE FROM expenses WHERE id = ?",
            (expense_id,),
        )
        return cursor.rowcount


@app.route("/")
def index():
    expenses = get_expenses()
    total_amount = sum(expense["amount"] for expense in expenses)
    return render_template(
        "index.html",
        categories=CATEGORIES,
        expenses=expenses,
        total_amount=total_amount,
    )


@app.post("/delete/<int:expense_id>")
def delete_expense(expense_id):
    deleted_count = remove_expense(expense_id)
    if deleted_count:
        flash("Expense deleted successfully.", "success")
    else:
        flash("Expense could not be found.", "error")
    return redirect(url_for("index"))


@app.route("/add", methods=["GET", "POST"])
def add_expense():
    form_data = {
        "title": "",
        "amount": "",
        "expense_date": date.today().isoformat(),
        "category": CATEGORIES[0],
    }

    if request.method == "POST":
        form_data = {
            "title": request.form.get("title", "").strip(),
            "amount": request.form.get("amount", "").strip(),
            "expense_date": request.form.get("expense_date", "").strip(),
            "category": request.form.get("category", "").strip(),
        }
        errors = []

        if not form_data["title"]:
            errors.append("Expense title is required.")

        try:
            amount = float(form_data["amount"])
            if amount <= 0:
                errors.append("Amount must be greater than zero.")
        except ValueError:
            errors.append("Amount must be a valid number.")
            amount = 0

        if not form_data["expense_date"]:
            errors.append("Date is required.")

        if form_data["category"] not in CATEGORIES:
            errors.append("Choose a valid category.")

        if errors:
            for error in errors:
                flash(error, "error")
            return render_template(
                "add_expense.html",
                categories=CATEGORIES,
                form_data=form_data,
            )

        create_expense(
            form_data["title"],
            amount,
            form_data["expense_date"],
            form_data["category"],
        )
        flash("Expense added successfully.", "success")
        return redirect(url_for("index"))

    return render_template(
        "add_expense.html",
        categories=CATEGORIES,
        form_data=form_data,
    )


if __name__ == "__main__":
    app.run(debug=True)
```

### `templates/base.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block title %}Expense Tracker{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
  </head>
  <body>
    <header class="site-header">
      <nav class="nav">
        <a class="brand" href="{{ url_for('index') }}">Expense Tracker</a>
        <div class="nav-links" aria-label="Primary navigation">
          <a href="{{ url_for('index') }}">Expenses</a>
          <a class="nav-button" href="{{ url_for('add_expense') }}">Add Expense</a>
        </div>
      </nav>
    </header>

    <main class="page">
      {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
          <div class="flash-stack" role="status" aria-live="polite">
            {% for category, message in messages %}
              <div class="flash flash-{{ category }}">{{ message }}</div>
            {% endfor %}
          </div>
        {% endif %}
      {% endwith %}

      {% block content %}{% endblock %}
    </main>
  </body>
</html>
```

### `templates/index.html`

```html
{% extends "base.html" %}

{% block content %}
  <section class="hero">
    <div>
      <p class="eyebrow">Personal finance</p>
      <h1>Track daily spending clearly.</h1>
      <p class="intro">Review every saved expense by date, category, title, and amount.</p>
      <a class="primary-link" href="{{ url_for('add_expense') }}">Add Expense</a>
    </div>
    <div class="summary-box" aria-label="Expense summary">
      <span>Total Spent</span>
      <strong>Rs. {{ "%.2f"|format(total_amount) }}</strong>
    </div>
  </section>

  <section class="panel">
    <div class="section-header">
      <div>
        <p class="eyebrow">Expenses</p>
        <h2>All Expenses</h2>
      </div>
      <span class="count-pill">{{ expenses|length }} saved</span>
    </div>

    {% if expenses %}
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Title</th>
              <th>Category</th>
              <th>Date</th>
              <th class="amount-cell">Amount</th>
              <th class="action-cell">Action</th>
            </tr>
          </thead>
          <tbody>
            {% for expense in expenses %}
              <tr>
                <td data-label="Title">{{ expense["title"] }}</td>
                <td data-label="Category">
                  <span class="category-chip">{{ expense["category"] }}</span>
                </td>
                <td data-label="Date">{{ expense["expense_date"] }}</td>
                <td data-label="Amount" class="amount-cell">Rs. {{ "%.2f"|format(expense["amount"]) }}</td>
                <td data-label="Action" class="action-cell">
                  <form
                    action="{{ url_for('delete_expense', expense_id=expense['id']) }}"
                    method="post"
                    onsubmit="return confirm('Delete this expense?');"
                  >
                    <button class="danger-button" type="submit">Delete</button>
                  </form>
                </td>
              </tr>
            {% endfor %}
          </tbody>
        </table>
      </div>
    {% else %}
      <div class="empty-state">
        <h3>No expenses yet</h3>
        <p>Add your first expense to start tracking spending by date and category.</p>
        <a class="primary-link" href="{{ url_for('add_expense') }}">Add Expense</a>
      </div>
    {% endif %}
  </section>
{% endblock %}
```

### `templates/add_expense.html`

```html
{% extends "base.html" %}

{% block title %}Add Expense | Expense Tracker{% endblock %}

{% block content %}
  <section class="hero compact-hero">
    <div>
      <p class="eyebrow">New expense</p>
      <h1>Add Expense</h1>
      <p class="intro">Record the title, amount, date, and category for a spending entry.</p>
    </div>
  </section>

  <section class="panel form-panel">
    <form action="{{ url_for('add_expense') }}" method="post">
      <div class="form-grid">
        <label>
          <span>Expense Title</span>
          <input
            type="text"
            name="title"
            value="{{ form_data.title }}"
            placeholder="Groceries"
            maxlength="120"
            required
          >
        </label>

        <label>
          <span>Amount</span>
          <input
            type="number"
            name="amount"
            value="{{ form_data.amount }}"
            min="0.01"
            step="0.01"
            placeholder="499.00"
            required
          >
        </label>

        <label>
          <span>Date</span>
          <input
            type="date"
            name="expense_date"
            value="{{ form_data.expense_date }}"
            required
          >
        </label>

        <label>
          <span>Category</span>
          <select name="category" required>
            {% for category in categories %}
              <option value="{{ category }}" {% if form_data.category == category %}selected{% endif %}>
                {{ category }}
              </option>
            {% endfor %}
          </select>
        </label>
      </div>

      <div class="form-actions">
        <a class="secondary-link" href="{{ url_for('index') }}">Cancel</a>
        <button type="submit">Save Expense</button>
      </div>
    </form>
  </section>
{% endblock %}
```

### `static/styles.css`

```css
:root {
  color-scheme: light;
  --bg: #f6f7f9;
  --surface: #ffffff;
  --surface-muted: #eef3f5;
  --text: #1f2933;
  --muted: #667085;
  --line: #d7dee4;
  --accent: #197278;
  --accent-strong: #12585d;
  --danger: #b42318;
  --danger-bg: #fff1f0;
  --shadow: 0 16px 40px rgba(31, 41, 51, 0.08);
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  min-height: 100vh;
  background: var(--bg);
  color: var(--text);
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.5;
}

a {
  color: inherit;
}

.site-header {
  background: var(--surface);
  border-bottom: 1px solid var(--line);
}

.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: min(1080px, calc(100% - 32px));
  margin: 0 auto;
  min-height: 64px;
}

.brand {
  color: var(--text);
  font-size: 1.1rem;
  font-weight: 700;
  text-decoration: none;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 12px;
}

.nav-links a {
  color: var(--muted);
  font-weight: 700;
  text-decoration: none;
}

.nav-links a:hover {
  color: var(--accent);
}

.nav-button,
.primary-link,
.secondary-link,
button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 42px;
  padding: 9px 14px;
  border-radius: 8px;
  font-weight: 700;
  text-decoration: none;
}

.nav-button,
.primary-link,
button {
  background: var(--accent);
  border: 1px solid var(--accent);
  color: #ffffff;
}

.nav-button:hover,
.primary-link:hover,
button:hover {
  background: var(--accent-strong);
  color: #ffffff;
}

.danger-button {
  min-height: 36px;
  padding: 7px 12px;
  background: var(--danger-bg);
  border-color: #f4b7b2;
  color: var(--danger);
}

.danger-button:hover {
  background: var(--danger);
  border-color: var(--danger);
  color: #ffffff;
}

.secondary-link {
  background: var(--surface);
  border: 1px solid var(--line);
  color: var(--text);
}

button {
  cursor: pointer;
  font: inherit;
}

.page {
  width: min(1080px, calc(100% - 32px));
  margin: 0 auto;
  padding: 32px 0 48px;
}

.hero {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(220px, 320px);
  gap: 24px;
  align-items: end;
  padding: 32px 0;
}

.compact-hero {
  grid-template-columns: 1fr;
  padding-bottom: 20px;
}

.eyebrow {
  margin: 0 0 8px;
  color: var(--accent);
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
}

h1,
h2,
h3,
p {
  margin-top: 0;
}

h1 {
  max-width: 760px;
  margin-bottom: 12px;
  font-size: clamp(2rem, 6vw, 4.5rem);
  line-height: 1;
}

h2 {
  margin-bottom: 18px;
  font-size: 1.25rem;
}

.intro {
  max-width: 640px;
  color: var(--muted);
  font-size: 1.05rem;
}

.hero .primary-link {
  margin-top: 8px;
}

.flash-stack {
  display: grid;
  gap: 10px;
  margin-bottom: 20px;
}

.flash {
  border-radius: 8px;
  padding: 12px 14px;
  font-weight: 700;
}

.flash-success {
  background: #e6f4f1;
  border: 1px solid #b7ded6;
  color: var(--accent-strong);
}

.flash-error {
  background: var(--danger-bg);
  border: 1px solid #f4b7b2;
  color: var(--danger);
}

.panel {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 8px;
  box-shadow: var(--shadow);
  padding: 24px;
}

.summary-box {
  display: grid;
  gap: 8px;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 8px;
  box-shadow: var(--shadow);
  padding: 22px;
}

.summary-box span {
  color: var(--muted);
  font-size: 0.9rem;
  font-weight: 700;
}

.summary-box strong {
  color: var(--accent);
  font-size: 2rem;
}

.section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 18px;
}

.section-header h2 {
  margin-bottom: 0;
}

.count-pill {
  display: inline-flex;
  align-items: center;
  min-height: 34px;
  padding: 6px 12px;
  background: #e6f4f1;
  border: 1px solid #b7ded6;
  border-radius: 999px;
  color: var(--accent-strong);
  font-size: 0.9rem;
  font-weight: 700;
  white-space: nowrap;
}

.table-wrap {
  overflow-x: auto;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 14px 12px;
  border-bottom: 1px solid var(--line);
  text-align: left;
  vertical-align: middle;
}

th {
  color: var(--muted);
  font-size: 0.78rem;
  text-transform: uppercase;
}

tbody tr:last-child td {
  border-bottom: 0;
}

.amount-cell {
  text-align: right;
  font-weight: 700;
}

.action-cell {
  text-align: right;
}

.action-cell form {
  display: inline-flex;
}

.empty-state {
  min-height: 180px;
  display: grid;
  place-items: center;
  padding: 32px;
  background: var(--surface-muted);
  border: 1px dashed var(--line);
  border-radius: 8px;
  text-align: center;
}

.empty-state h3 {
  margin-bottom: 6px;
}

.empty-state p {
  max-width: 420px;
  margin-bottom: 0;
  color: var(--muted);
}

.empty-state .primary-link {
  margin-top: 14px;
}

.form-panel {
  max-width: 820px;
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
}

label {
  display: grid;
  gap: 8px;
  color: var(--text);
  font-weight: 700;
}

input,
select {
  width: 100%;
  min-height: 46px;
  padding: 10px 12px;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 8px;
  color: var(--text);
  font: inherit;
}

input:focus,
select:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(25, 114, 120, 0.16);
  outline: none;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 24px;
}

.category-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.category-chip {
  display: inline-flex;
  align-items: center;
  min-height: 36px;
  padding: 6px 12px;
  background: var(--surface-muted);
  border: 1px solid var(--line);
  border-radius: 999px;
  color: var(--text);
  font-weight: 700;
}

@media (max-width: 640px) {
  .nav,
  .page {
    width: min(100% - 24px, 1080px);
  }

  .nav {
    align-items: flex-start;
    flex-direction: column;
    justify-content: center;
    gap: 10px;
    padding: 14px 0;
  }

  .nav-links {
    width: 100%;
    justify-content: space-between;
  }

  .page {
    padding-top: 20px;
  }

  .hero {
    grid-template-columns: 1fr;
    padding-top: 18px;
  }

  .panel {
    padding: 18px;
  }

  .form-grid {
    grid-template-columns: 1fr;
  }

  .form-actions {
    flex-direction: column-reverse;
  }

  .form-actions a,
  .form-actions button {
    width: 100%;
  }

  .section-header {
    align-items: flex-start;
    flex-direction: column;
  }

  table,
  thead,
  tbody,
  tr,
  th,
  td {
    display: block;
  }

  thead {
    display: none;
  }

  tr {
    border-bottom: 1px solid var(--line);
    padding: 12px 0;
  }

  tbody tr:last-child {
    border-bottom: 0;
  }

  td {
    display: flex;
    justify-content: space-between;
    gap: 16px;
    border-bottom: 0;
    padding: 8px 0;
    text-align: right;
  }

  td::before {
    content: attr(data-label);
    color: var(--muted);
    font-weight: 700;
    text-align: left;
  }

  .amount-cell {
    text-align: right;
  }

  .action-cell {
    text-align: right;
  }
}
```
