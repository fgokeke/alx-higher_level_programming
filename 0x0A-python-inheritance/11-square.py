#!/usr/bin/python3
"""To define a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square (Rectangle):
    """To represent a square"""
    def __init__(self, size):
        """
        To initialize the size of a square.

        Args:
        size (int): the size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
