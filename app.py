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
