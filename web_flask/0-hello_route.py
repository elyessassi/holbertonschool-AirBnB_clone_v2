#!/usr/bin/python3
"""create a test server that displays hello hbnb"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)

def home():
    """page displays hello hbnb"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run()

