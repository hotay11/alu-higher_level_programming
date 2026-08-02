#!/usr/bin/python3
"""Module that prints text with indentation after . ? and :."""


def text_indentation(text):
    """Print text, adding two newlines after each ., ? or : found.

    Args:
        text: the string to print, must be a string.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
    lines = [line.strip() for line in result.split("\n")]
    output = "\n".join(lines)
    print(output.rstrip("\n"), end="")
