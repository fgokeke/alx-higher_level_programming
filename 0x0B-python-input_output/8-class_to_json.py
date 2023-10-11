#!/usr/bin/python3
"""a function that returns the dictionary description with simple data
structure (list, dictionary, string, integer and boolean) for JSON
serialization of an object"""


def class_to_json(obj):
    """
    Serialize an object to a JSON-serializable dictionary.

    Parameters:
    obj: An instance of a class with serializable attributes.

    Returns:
    dict: A dictionary representation of the object
    suitable for JSON serialization.
    """
    if not hasattr(obj, '__dict__'):
        return ({})
    serialized_data = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized_data[key] = value
    return (serialized_data)
