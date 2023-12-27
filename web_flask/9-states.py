#!/usr/bin/python3
""" This module starts a Flask web application
    that listens on a localhost port 5000
    """
from flask import Flask, render_template
from models import storage
from markupsafe import escape
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def display_states():
    """Show the states from the DB"""
    states = storage.all(State).values()
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def display_state(id):
    """Show a state from the DB"""
    state = storage.all(State).get("State.{}".format(escape(id)))
    print(state)
    return render_template("9-states.html", state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
