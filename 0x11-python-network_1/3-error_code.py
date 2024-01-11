#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).
Handles urllib.error.HTTPError exceptions and prints the HTTP status code.
"""


import urllib.request
import urllib.error
import sys


def fetch_url(url):
    """
    Fetches the content of a URL and prints it.

    Args:
        url (str): The URL to fetch.

    Raises:
        urllib.error.HTTPError: If an HTTP error occurs.
    """
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
