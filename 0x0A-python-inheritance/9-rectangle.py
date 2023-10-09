#!/usr/bin/python3
"""To define a class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """To represent a rectangle."""
    def __init__(self, width, height):
        """
        To initialize the width and height.

        Args:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """To calculate and return area of rectangle."""
        return (self.__width * self.__height)

    def __str__(self):
        """To return the print() and str() representation of a Rectangle."""
        rec_string = "[" + str(self.__class__.__name__) + "] "
        rec_string += str(self.__width) + "/" + str(self.__height)
        return (rec_string)
