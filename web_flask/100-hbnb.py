#!/usr/bin/python3
""" This module starts a Flask web application
    that listens on a localhost port 5000
    """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def display_state_city_amenity_place():
    """Show the states, cities, ameities, and places from the DB"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template("100-hbnb.html", states=states,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
