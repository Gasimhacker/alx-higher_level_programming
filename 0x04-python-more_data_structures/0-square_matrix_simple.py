#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix."""

    sqr_matrix = [[x ** 2 for x in a_list] for a_list in matrix]
    return sqr_matrix
