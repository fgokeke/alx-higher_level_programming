#!/usr/bin/python3
""" a function that returns an object (Python data structure)
represented by a JSON string"""
import json


def from_json_string(my_str):
    """
    Parse a JSON string and return the corresponding Python data structure.

    Parameters:
    my_str (str): The JSON string to be parsed.

    Returns:
    object: The Python data structure represented by the JSON string.
    """
    return (json.loads(my_str))
