#!/usr/bin/python3
""" This module starts a Flask web application
    that listens on a localhost port 5000
    """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def say_hello():
    """say hello to a user"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
