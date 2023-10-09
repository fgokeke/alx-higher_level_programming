#!/usr/bin/python3
"""A function that returns the list of available
attributes and methods of an object"""


def lookup(obj):
    """
    A function that returns the list of available
    attributes and methods of an object.

    Args:
    obj (object): the object to consider.

    Returns:
    list: a list of attributes and method names.
    """
    attr_and_meth = []
    for name in dir(obj):
        attr_and_meth.append(name)
    return (attr_and_meth)
