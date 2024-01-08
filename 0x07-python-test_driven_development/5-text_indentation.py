#!/usr/bin/python3
"""

This module contains of a function that adds two lines
after each of the ['.', '?', ':'] characters

"""


def text_indentation(text):
    """

    A function that adds two lines
    after each of the ['.', '?', ':'] characters

    Args:
        text: The text that should be edited

    Raises:
        TypeError: If text isn't a string

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    ans = ""
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        ans += text[c]
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                ans += "\n\n"
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1

    ans = ans.strip(" ")

    print(ans, end="")
