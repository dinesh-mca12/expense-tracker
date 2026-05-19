import sqlite3
from pathlib import Path

from flask import Flask, render_template


app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
