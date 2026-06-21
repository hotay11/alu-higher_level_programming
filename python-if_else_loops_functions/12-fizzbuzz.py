#!/usr/bin/python3
"""Module that prints numbers 1 to 100 with FizzBuzz rules."""


def fizzbuzz():
    """Print numbers 1-100, replacing multiples of 3/5 with Fizz/Buzz."""
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
