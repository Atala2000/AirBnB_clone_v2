#!/usr/bin/python3
""" starts a Flask web application"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """
    display “C ” followed by the value of the text
    """
    return "C {}".format(text.replace("_", ""))


@app.route("/python/<text>", strict_slashes=False)
def display_python(text="is cool"):
    return "Python {}".format(text.replace("_", ""))


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:number>", strict_slashes=False)
def html_page(number):
    return render_template("5-number.html", number=number)


if __name__ == "__main__":
    """Run the Flask app on 0.0.0.0, port 5000"""
    app.run(host="0.0.0.0", port=5000)
