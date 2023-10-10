#!/usr/bin/python3
""" a function that returns the JSON
representation of an object (string)"""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object as a string.

    Parameters:
    my_obj: The object to be converted to JSON.

    Returns:
    str: The JSON representation of the object.
    """
    return (json.dumps(my_obj))
