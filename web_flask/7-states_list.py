#!/usr/bin/python3
""" This module starts a Flask web application
    that listens on a localhost port 5000
    """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_states():
    """Show the states from the DB"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)
