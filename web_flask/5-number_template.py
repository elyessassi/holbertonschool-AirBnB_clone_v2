#!/usr/bin/python3
"""create a test server that displays hello hbnb and hbnb"""
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """page displays hello hbnb"""

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display HBNB"""

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """display c with the text string"""

    text = text.replace("_", " ")
    return f"C {escape(text)}"


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>")
def python(text):
    """display Python with text string with default value is cool"""

    text = text.replace("_", " ")
    return f"Python {escape(text)}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display the number n if n is an int"""

    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """renders template that containes n"""

    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run()
