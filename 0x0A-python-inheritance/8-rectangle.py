#!/usr/bin/python3
"""To define a class BaseGeometry."""


class BaseGeometry:
    """To represent base geometry."""
    def area(self):
        """
        raises an Exception with the
        message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value.

        Args:
        name (str): the parameter name.
        value (int): the paramter to validate.

        Raises:
        TypeError: if value is not an integer.
        ValueError: if value is less or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
