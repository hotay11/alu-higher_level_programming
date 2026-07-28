#!/usr/bin/python3
"""Module for Student class"""


class Student:
    """A Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of Student"""
        return self.__dict__
