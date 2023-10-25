#!/usr/bin/python3

"""Class named Square with a specific size"""


class Square:
    """ A class that defines a square with specific size"""

    def __init__(self, size=0):
        """Initialize the Square class with a size that has a positive value"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ Compute the area of the square object"""

        return (self.__size ** 2)
