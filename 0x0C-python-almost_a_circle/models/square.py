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

    @property
    def size(self):
        """Get the size of the square."""
        return (self.width)

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assign attributes based on *args and **kwargs.

        Args:
            *args: List of arguments - no-keyworded arguments.
            **kwargs: Double pointer to a dictionary representing
            key/value (keyworded arguments).
        """
        if args:
            for i, attr in enumerate(args[:4]):
                setattr(self, ['id', 'size', 'x', 'y'][i], attr)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

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

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Square.
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
