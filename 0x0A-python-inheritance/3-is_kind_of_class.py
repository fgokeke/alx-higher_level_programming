#!/usr/bin/python3
"""a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if it's an instance
    of a class that inherited from, the specified class.

    Args:
    obj (object): The object to be checked.
    a_class (type): The class to compare with.

    Returns:
    bool: True if the object is an instance of the specified
    class or its subclasses, otherwise False.
    """
    if isinstance(obj, a_class):
        return (True)
    return (False)
