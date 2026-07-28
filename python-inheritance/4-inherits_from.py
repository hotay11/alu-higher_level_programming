#!/usr/bin/python3
"""Module for inherits_from function"""


def inherits_from(obj, a_class):
    """Returns True if obj inherited from a_class but is not a_class itself"""
    return isinstance(obj, a_class) and type(obj) is not a_class
