#!/usr/bin/python3
"""A python script with a class Square
that defines a square"""

class Square:
    """a class Square that defines a square."""

    def __init__(self, size=0):
        """To initialize a new square.

        Args:
            size (int): size of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
