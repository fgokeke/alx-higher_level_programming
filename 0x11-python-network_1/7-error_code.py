#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL,
and displays the body of the response.
Prints an error message if the HTTP status code is
greater than or equal to 400.
"""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.HTTPError as e:
        print("Error code:", e.response.status_code)
