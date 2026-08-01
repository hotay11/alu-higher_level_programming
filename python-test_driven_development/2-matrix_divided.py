#!/usr/bin/python3
"""Module that divides all elements of a matrix by a divisor."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div, rounded to 2 decimals.

    Args:
        matrix: a list of lists of ints or floats, rows must be equal size.
        div: the divisor, must be an int or float and not zero.

    Returns:
        A new matrix with each element divided by div.

    Raises:
        TypeError: if matrix is not a list of lists of ints/floats,
            if rows differ in size, or if div is not a number.
        ZeroDivisionError: if div is 0.
    """
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) == 0 or not all(
                isinstance(n, (int, float)) and not isinstance(n, bool)
                for n in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(n / div, 2) for n in row] for row in matrix]
