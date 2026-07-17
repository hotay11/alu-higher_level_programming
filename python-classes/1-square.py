#!/usr/bin/python3
"""This module defines a class Square that represents a square."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: The size of the new square.
        """
        self.__size = size
