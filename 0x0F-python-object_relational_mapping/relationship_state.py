#!/usr/bin/python3

"""
Create the class State that will map to a table of the same name
in the database

 Args:
    Base: The base class from which the State classe should inherit.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from relationship_city import Base, City


class State(Base):
    """ A class that information about states
        Args:
            id (int): The state id
            name (str): The state's name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship('City', backref="state", cascade="all, delete")
