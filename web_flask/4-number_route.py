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
    """
    Returns if a digit
    Args:
        n: the number
    """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
