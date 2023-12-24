#!/usr/bin/python3
""" This module starts a Flask web application
    that listens on a localhost port 5000
    """
from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def say_hello():
    """say hello to a user"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def say_hbnb():
    """say HBNB to a user"""
    return "HBNB!"


@app.route("/c/<text>", strict_slashes=False)
def say_c(text):
    """say C and custom text to a user"""
    return "C {}".format(escape(text.replace("_", " ")))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def say_python(text="is cool"):
    """say Python and custom text to a user"""
    return "Python {}".format(escape(text.replace("_", " ")))


@app.route("/number/<int:n>", strict_slashes=False)
def say_number(n):
    """say a number to a user"""
    return "{} is a number".format(escape(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def render_number(n):
    """say a number to a user"""
    return render_template("5-number.html", n=escape(n))


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def say_odd_or_even(n):
    """say a number to a user"""
    n = escape(n)
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
