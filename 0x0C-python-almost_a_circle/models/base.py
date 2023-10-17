#!/usr/bin/python3
"""Defines the base class of other classes in this project"""
import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string into a list of dictionaries.

        Args:
            json_string (str): The JSON string to be converted.

        Returns:
            list: The list of dictionaries represented by the JSON string.
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instances to a JSON file.

        Args:
            cls: The class (e.g., Rectangle or Square).
            list_objs (list): A list of instances to be saved to the JSON file.

        Notes:
            If list_objs is None, it initializes an empty list.
        """
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        json.data = cls.to_json_string([obj.to_dictionary() for
                                        obj in list_objs])
        filename = f"{class_name}.json"
        with open(filename,  'w', encoding="utf-8") as file:
            file.write(json.data)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes from a dictionary.

        Args:
            **dictionary: A double pointer to a dictionary
            containing attribute values.

        Returns:
            Instance: An instance with attributes set based on the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a JSON file.

        Returns:
            list: A list of instances loaded from the JSON file.
        """
        file_name = cls.__name__ + ".json"
        instances = []
        if os.path.exists(file_name):
            with open(file_name, "r", encoding="utf-8") as file:
                json_data = file.read()
                dictionaries = Base.from_json_string(json_data)
                for dictionary in dictionaries:
                    instance = cls.create(**dictionary)
                    instances.append(instance)

        return (instances)
