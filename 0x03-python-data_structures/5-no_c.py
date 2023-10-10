#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for ch in (my_string):
        if (ch != 'C' and ch != 'c'):
            new_string += ch
    return (new_string)
