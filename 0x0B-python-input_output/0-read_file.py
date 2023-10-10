#!/usr/bin/python3
"""Write a function that reads a text file
(UTF8) and prints it to stdout"""


def read_file(filename=""):
    """
    Read a UTF-8 text file and print its contents to stdout.

    Parameters:
    filename (str): The name of the file to be read.

    Returns:
    None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
