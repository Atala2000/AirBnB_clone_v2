from flask import Flask, render_template

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
def hbnb():
    """
    Create route for /hbnb
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """
    Returns user specified route
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
    return f"{n} is a number"


@app.route("/number_template/<int:number>", strict_slashes=False)
def template(number):
    """
    Args:
        number: digit to return as an argument
    """
    return render_template("5-number.html", number=number)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    """
    Args:
        n: numberthat acts as argument
    """
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
