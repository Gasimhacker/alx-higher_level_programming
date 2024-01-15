#!/usr/bin/python3

"""A module containing the Base class for all next
implemented classes"""

import json


class Base:
    """

    A base class for other classes like
    Rectangle and Square classes

    Args:
        __nb_objects (int): The number of base class objects

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class with a specific id

        Args:
            id (int): The object's id

        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries

        Args:
            list_dictionaries (list): A list of dictionaries

        Returns:
            The JSON string representation
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
