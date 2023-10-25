#!/usr/bin/python3
"""A Module that DEFINES a MagicClass matching alx bytecode task"""

import math


class MagicClass:
    """A Class REPRESENTING a circle apparently"""

    def __init__(self, radius=0):
        """Initialize a MagicClass
        Arg:
            radius (float or int): The radius of the new circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the circle"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the circle"""
        return (2 * math.pi * self.__radius)
