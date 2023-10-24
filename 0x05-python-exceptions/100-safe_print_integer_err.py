#!/usr/bin/python3

def safe_print_integer_err(value):
    """Print the value if its an integer."""

    from sys import stderr

    try:
        print("{:d}".format(value))
        return (True)
    except Exception as e:
        print("Exception: {}".format(e), file=stderr)
        return (False)
