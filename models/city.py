#!/usr/bin/python
""" holds class City"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models import env_storage



class City(BaseModel, Base):
    """Representation of city """
    if env_storage == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
       
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)