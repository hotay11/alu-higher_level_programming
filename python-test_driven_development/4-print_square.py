#!/usr/bin/python3
"""Module that prints a square of #."""


def print_square(size):
    """Print a square of size x size using the # character.

    Args:
        size: the length of a side of the square, must be an int >= 0.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
