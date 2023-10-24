#!/usr/bin/python3

def safe_print_division(a, b):
    """Divide 2 integers and prints the result."""

    try:
        result = a / b
        return (True)
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result:{}".format(result))
        return (result)
