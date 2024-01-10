#!/usr/bin/python3

"""A module for finding the pascal triangle of any length"""


def pascal_triangle(n):
    """Represent the pascal’s triangle of height n

    Args:
        n (int): The height of the triangle

    Returns:
        A list of lists of integers representing the Pascal’s triangle
    """
    tri = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j in [0, i]:
                row.append(1)
            else:
                col = tri[i - 1][j - 1] + tri[i - 1][j]
                row.append(col)
        tri.append(row)
    return tri
