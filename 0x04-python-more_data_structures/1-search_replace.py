#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""

    new_list = [item if item != search else replace for item in my_list]
    return new_list
