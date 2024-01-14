#!/usr/bin/python3

"""A module containing the Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """
    A Rectangle class

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the class with a specific id

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): The x coordinate of the rectangle
            y (int): The y coordinate of the rectangle
            id (int): The rectangle's id

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """Set/get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def width(self):
        """Set/get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def x(self):
        """Set/get the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        """Set/get the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
