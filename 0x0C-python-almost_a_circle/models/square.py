#!/usr/bin/python3
"""A class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle and represents a
    square with the same width and height.

    Attributes:
        size (int): The size of the square.

    Args:
        size (int): The size of the square.
        x (int, optional): The x-coordinate of the square's
        position (default is 0).
        y (int, optional): The y-coordinate of the
        square's position (default is 0).
        id (int, optional): An optional integer value
        to assign as the 'id' attribute.

    Methods:
        None
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the
            square's position (default is 0).
            y (int, optional): The y-coordinate of the
            square's position (default is 0).
            id (int, optional): An optional integer
            value to assign as the 'id' attribute.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return the string representation of the Square instance.

        Returns:
            str: A string in the format
            [Square] (<id>) <x>/<y> - <size>.
        """
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
            )
