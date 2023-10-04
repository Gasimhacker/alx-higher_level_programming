#!/usr/bin/python3
def remove_char_at(str, n):
    """Remove the character at the given index."""
    if (n < 0):
        return (str)
    return (str[:n] + str[n + 1:])
