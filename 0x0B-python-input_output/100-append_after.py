#!/usr/bin/python3

"""This module contains a function that insert texts to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Insert lines of text to a file

    Args:
        filename (str): The path to the file
        search_string (str): The string to search and modify its line
        new_string (str): The inserted string

    """

    lines = ""

    with open(filename, "r", encoding="UTF8") as f:
        for line in f:
            if search_string in line:
                line += new_string
            lines += line

    with open(filename, "w", encoding="UTF8") as f:
        f.write(lines)
