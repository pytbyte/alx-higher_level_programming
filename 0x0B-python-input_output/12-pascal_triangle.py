#!/usr/bin/python3
"""
function Pascal's Triangle

"""


def pascal_triangle(n):
    """
    Function that returns a list of
    lists of integers representing the
    Pascal’s triangle of n
    """

    if n <= 0:
        return []

    shape = [[1]]

    for x in range(1, n):
        row = [1]
        for y in range(1, x):
            row.append(shape[x-1][y-1] + shape[x-1][y])
        row.append(1)
        shape.append(row)
    return shape
