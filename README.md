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

## Setup

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in your browser.
