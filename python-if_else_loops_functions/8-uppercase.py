#!/usr/bin/python3
"""Module that prints a string in uppercase."""


def uppercase(str):
    """Print a string in uppercase, followed by a new line."""
    result = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
