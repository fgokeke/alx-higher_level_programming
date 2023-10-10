#!/usr/bin/python3
"""a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """
    Create a Python object from a JSON file.

    Parameters:
    filename (str): The name of the JSON file to load.

    Returns:
    object: The Python object created from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return (json.load(file))
