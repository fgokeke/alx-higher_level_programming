#!/usr/bin/python3
"""a function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified
class ; otherwise False."""


def inherits_from(obj, a_class):
    """
    checks if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class

    Args:
    obj (object): The object to be checked.
    a_class (type): The class to compare with.

    Returns:
    bool: True if the object is an instance of a class that
    inherited from the specified class, otherwise False.
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return (True)
    return (False)
