#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Return a set of common elements in two sets"""

    ans = (x for x in set_1 if x in set_2)
    return ans
