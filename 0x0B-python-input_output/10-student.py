#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student:
    """
    Defines a Student by first_name, last_name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.

        Parameters:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Parameters:
        attrs (list): A list of attribute names to include in the dictionary.
                      If None, all attributes are included.

        Returns:
        dict: A dictionary containing the student's attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            filtered_data = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_data[attr] = getattr(self, attr)
            return (filtered_data)
