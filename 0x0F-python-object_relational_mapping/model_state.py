#!/usr/bin/python3
"""
Contains the class definition of a State and an
instance Base = declarative_base()
"""


from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

my_metadata = MetaData()
Base = declarative_base(metadata=my_metadata)


class State(Base):
    """
    State Class with class attribtues id and name.
    """
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
