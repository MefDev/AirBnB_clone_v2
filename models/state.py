#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Index
from sqlalchemy.orm import relationship
from models import env_storage, storage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    if (env_storage == 'db'):
        __tablename__ = "states"
        name = Column(String(128), nullable=False, unique=True)
        cities = relationship('City', backref="state", cascade="all, delete-orphan")
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
    
    if env_storage != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

    
