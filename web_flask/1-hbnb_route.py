#!/usr/bin/python3
"""Starts a Flask web application.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Def doc."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")