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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
