#!/usr/bin/python3
"""
A function that divides all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """
    divides matrix by scalar integer, rounded to two decimal places

    """
    import decimal
    type_error = "matrix must be a matrix list of integers/floats"
    if type(matrix) is not list:
        raise TypeError()
    rosw_len = []
    rosw_conter = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(type_error)
        rosw_len.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(type_error)
        rosw_conter += 1
    if any(len(row) != rosw_len[0] for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = list(map(lambda row:
                          list(map(lambda x: round(x/div, 2), row)), matrix))
    return new_matrix
