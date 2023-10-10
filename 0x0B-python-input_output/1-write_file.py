#!/usr/bin/python3
"""a function that writes a string to a
text file (UTF8) and returns the number of characters written"""


def write_file(filename="", text=""):
    """
    Write a string to a UTF-8 text file and return the number of characters written.

    Parameters:
    filename (str): The name of the file to write to.
    text (str): The string to be written to the file.

    Returns:
    int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        characters_written = file.write(text)
        return (characters_written)
