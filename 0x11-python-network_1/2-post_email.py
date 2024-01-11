#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response (decoded in utf-8).
"""


import urllib.parse
import urllib.request
import sys


def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the email as a parameter.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email parameter to include in the request.

    Returns:
        bytes: The body of the response.
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        return response.read()


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response_body = send_post_request(url, email)
    print(response_body.decode('utf-8'))
