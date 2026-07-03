#!/usr/bin/python3
""" Roman to Integer module
"""


def roman_to_int(roman_string):
    """ Converts a Roman numeral string to an integer """
    if not isinstance(roman_string, str):
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    for i in range(len(roman_string)):
        current_value = roman_values.get(roman_string[i], 0)
        if i + 1 < len(roman_string):
            next_value = roman_values.get(roman_string[i + 1], 0)
            if current_value < next_value:
                total -= current_value
            else:
                total += current_value
        else:
            total += current_value

    return total
