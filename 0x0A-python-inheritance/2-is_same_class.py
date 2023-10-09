#!/usr/bin/python3
"""a function that returns True if the object is exactly
an instance of the specified class ; otherwise False."""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
    obj (object): The object to be checked.
    a_class (type): The class to compare with.

    Returns:
    bool: True if the object is an instance of the
    specified class, otherwise False.
    """
    return (type(obj) == a_class)
