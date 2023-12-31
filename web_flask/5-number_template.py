#!/usr/bin/python3
"""
Module for creating Flask instance
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    Creates route for /
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Create route for /hbnb
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """
    Returns user specified route
    Args:
        text: the text that will be returned
    """
    changed_text = text.replace("_", " ")
    return f"C {changed_text}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python(text="is cool"):
    """
    Returns user specified route
    """
    changed_text = text.replace("_", " ")
    return f"Python {changed_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Returns if n is an integer
    Args:
        n: number
    """
    return f"{n} is a number"


@app.route("/number_template/<int:number>", strict_slashes=False)
def template(number):
    """
    Returns a template if number is an integer
    Args:
        number: The digit to check
    """
    return render_template("5-number.html", number=number)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
