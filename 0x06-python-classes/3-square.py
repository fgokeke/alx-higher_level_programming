#!/usr/bin/python3
"""A python script with class Square that defines a square by:
    (based on 2-square.py)"""


class Square:
    """A class Square that defines a square by:
        (based on 2-square.py)"""

    def __init__(self, size=0):
        """To initiliaze the new square

        Args:
            size (int): the size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """A function that calculates
        and returns the area of the current square."""
        return (self.__size * self.__size)
