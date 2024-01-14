#!/usr/bin/python3

"""A module containing the Base class for all next
implemented classes"""


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
