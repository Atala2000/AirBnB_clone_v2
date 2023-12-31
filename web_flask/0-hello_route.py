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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
