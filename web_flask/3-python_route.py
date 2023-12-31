#!/usr/bin/python3
"""
Module for creating Flask instance
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    Creates route for /
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def index_2():
    """
    Create route for /hbnb
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def index_3(text):
    """
    Returns user specified route
    """
    changed_text = text.replace("_", " ")
    return f"C {changed_text}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def index_4(text="is cool"):
    """
    Returns user specified route
    """
    changed_text = text.replace("_", " ")
    return f"Python {changed_text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
