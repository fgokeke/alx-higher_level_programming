#!/usr/bin/python3
"""Defines the base class of other classes in this project"""


class Base:
    """
    Base class for managing unique identifiers in the project.

    This class is intended to serve as a foundational
    component for other classes.
    It ensures that each instance has a unique 'id' attribute.

    Attributes:
        __nb_objects (int): A private class attribute to keep
        track of the total number of instances.

    Args:
        id (int, optional): An optional integer value to assign
        as the 'id' attribute.
        If not provided, the 'id' will be
        auto-incremented based on '__nb_objects'.

    Attributes:
        id (int): A public instance attribute representing
        the unique identifier for each instance
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int, optional): An optional integer value to assign
            as the 'id' attribute.
            If not provided, the 'id' will be auto-incremented
            based on '__nb_objects'.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
