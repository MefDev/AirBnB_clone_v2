#!/usr/bin/python3
""" This module starts a Flask web application
    that listens on a localhost port 5000
    """
from flask import Flask
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


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
