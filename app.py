from flask import Flask, render_template


app = Flask(__name__)

CATEGORIES = [
    "Food",
    "Travel",
    "Utilities",
    "Needs",
    "Wants",
    "Savings",
]


@app.route("/")
def index():
    return render_template("index.html", categories=CATEGORIES)


if __name__ == "__main__":
    app.run(debug=True)
