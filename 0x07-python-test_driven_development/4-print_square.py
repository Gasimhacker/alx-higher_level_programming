#!/usr/bin/python3
"""

This module contains a function that Print a square using
the '#' character

"""


def print_square(size):
    """

    Function that prints a square with the '#' character
    using the 'size' passed

    Args:
        Size (int): The size of the square

    Raises:
        TypeError: If size isn't an integer
        ValueError: If size is less than zero

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
