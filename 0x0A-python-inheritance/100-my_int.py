#!/usr/bin/python3


"""A module defining the "MyInt" class"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, other)
    """Return true if two instances are not equal"""

    return (int(str(self)) != int(str(other)))

    def __ne__(self, other)
    """Return true if two instances are not equal"""

    return (int(str(self)) == int(str(other)))
