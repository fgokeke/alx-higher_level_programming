#!/usr/bin/python3
"""a function that writes an Object to a text file,
using a JSON representation:"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON
    representation.

    Parameters:
    my_obj: The object to be written.
    filename (str): The name of the file to be written to.

    Returns:
    None.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
