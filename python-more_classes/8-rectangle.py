#!/usr/bin/python3
"""This module defines a class Rectangle that represents a rectangle."""


class Rectangle:
    """Represents a rectangle with private, validated width and height."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle. Defaults to 0.
            height (int): The height of the new rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the current width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the current height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the current area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """Return the current perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or
                height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Return the printable representation of the rectangle.

        Returns:
            str: The rectangle represented with the print_symbol
                character(s), or an empty string if width or
                height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rows = [
            str(self.print_symbol) * self.__width
            for i in range(self.__height)
        ]
        return "\n".join(rows)

    def __repr__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string that can be used with eval() to recreate
                a new instance with the same width and height.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message and decrement the instance count when
        an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle based on area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Raises:
            TypeError: If rect_1 is not an instance of Rectangle.
            TypeError: If rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: rect_1 if its area is greater than or equal
                to rect_2's area, otherwise rect_2.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
