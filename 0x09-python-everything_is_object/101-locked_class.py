#!/usr/bin/python3

"""

This module contains a class called locked class
that prevent creating a new instance attribute accidentally
when trying to access the attributes defined in the class

"""


class LockedClass:
    """

    This class will prevent the user from dynamically
    creating new instance attributes, except if
    the new instance attribute is called first_name
    """

    __slots__ = ["first_name"]
