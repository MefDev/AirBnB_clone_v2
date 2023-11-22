#!/usr/bin/python
""" holds class City"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import env_storage


class City(BaseModel, Base):
    """Representation of city """
    __tablename__ = 'cities'
    if env_storage == "db":
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
    else:
        state_id = ""
        name = ""
