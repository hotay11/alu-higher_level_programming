#!/usr/bin/python3
"""Module that prints the last digit of a number."""


def print_last_digit(number):
    """Print and return the last digit of a number."""
    last_digit = number % 10
    if number < 0:
        last_digit = (-number) % 10
    print(last_digit, end="")
    return last_digit
