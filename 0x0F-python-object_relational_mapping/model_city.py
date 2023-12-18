#!/usr/bin/python3
"""
Module that contains the class definition of a City.
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    City class with the following attributes:
    - id: auto-generated, unique integer, primary key
    - name: string of 128 characters, can't be null
    - state_id: integer, foreign key to states.id, can't be null
    """
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
