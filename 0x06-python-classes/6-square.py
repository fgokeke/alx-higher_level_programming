#!/usr/bin/python3
"""A python script with a class Square that defines a
square by: (based on 3-square.py)"""


class Square:
    """"Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """To initialize a new square.

        Args:
            size (int): Size of the square.
            position (int, int): position of the square.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """to retrieve the position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """to set the position of the square"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """returns the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return
        else:
            for i in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                for k in range(0, self.__size):
                    print("#", end="")
                print()
