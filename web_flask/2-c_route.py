#!/usr/bin/python3
from flask import Flask

"""
Module for creating Flask instance
"""
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
    changed_text = ""
    if "_" in text:
        changed_text = text.replace("_", " ")
    else:
        changed_text = text
    return f"C {changed_text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
