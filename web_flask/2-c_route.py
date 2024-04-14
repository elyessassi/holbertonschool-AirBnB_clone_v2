#!/usr/bin/python3
"""create a test server that displays hello hbnb and hbnb"""
from flask import Flask

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
    return f"c {text}"


if __name__ == "__main__":
    app.run()
