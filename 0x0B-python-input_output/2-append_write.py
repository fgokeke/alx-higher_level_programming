#!/usr/bin/python3
"""a function that appends a string to a
text file (UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """
    Append a string to a UTF-8 text file and return
    the number of characters added.

    Parameters:
    filename (str): The name of the file to add to.
    text (str): The string to be added to the file.

    Returns:
    int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        characters_added = file.write(text)
        return (characters_added)
