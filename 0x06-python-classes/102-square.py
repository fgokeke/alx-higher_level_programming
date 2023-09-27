#!/usr/bin/python3
"""A python script with a class Square that defines a
square by: (based on 3-square.py)"""


class Square:
    """"Defines a square"""

    def __init__(self, size=0):
        """To initialize a new square.

        Args:
            size (int): Size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """To retrieve the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """To set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """To return the current area of the square"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
