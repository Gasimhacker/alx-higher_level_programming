#!/usr/bin/python3
"""A Module that DEFINES a Square Class"""


class Square:
    """A Class that REPRESENTS a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance with
        a size that has a positive int value
        Args:
            size: a private instance attribure
            that holds the size of the square
        Raises:
            TypeError: if size isn't int
            ValueError: if size is negative"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        self.position = position

    def __str__(self):
        """A method to print square when using print"""
        return self.pos_print()[:-1]

    @property
    def size(self):
        """A Method that returns the size i.e
        getter
        Returns:
            size of square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """A Method that sets the size i.e
        setter
        Args:
            value: to set for size
        Raises:
            TypeError: if size isn't int
            ValueError: if size is negative"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of a square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """A Method that returns the area
        of the square
        Returns:
            area of the square
        """

        return self.__size ** 2

    def pos_print(self):
        """A Method that returns the position in
        spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """A Method to print the square in position"""
        print(self.pos_print(), end='')
