#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """A base geometry class"""

    def area(self):
        """Raises an Exception as area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value is a positive integer"""
        if type(value) is not int or type(value) is bool:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
