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
