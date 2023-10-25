#!/usr/bin/python3
"""A Module that DEFINES a Square Class"""


class Square:
    """A Class that REPRESENTS a Square"""

    def __init__(self, size=0):
        """Initialize a Square instance with
        a size that has a positive int value
        Args:
            size: a private instance attribure
            that holds the size of the square"""
        self.__size = size

    @property
    def size(self):
        """"A Method that returns the size i.e
        getter
        Returns:
            size of square
        Raises:
            TypeError: if size != int
            ValueErrorr: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """A Method that returns the area
        of the square
        Returns:
            area of the square
        """
        return self.__size ** 2

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()
