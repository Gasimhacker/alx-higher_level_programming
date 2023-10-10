#!/usr/bin/python3
def max_integer(my_list=[]):
    """Write a function that finds the biggest integer of a list."""

    if my_list is None:
        return None
    max_num = None
    for num in my_list:
        if num > max_num:
            max_num = num
    return (max_num)
