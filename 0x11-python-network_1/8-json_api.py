#!/usr/bin/python3
"""
Script that takes in a letter, sends a POST
request to http://0.0.0.0:5000/search_user,
and displays the response based on the given conditions.
"""


import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    try:
        response = requests.post(url, data={'q': letter})
        response.raise_for_status()

        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get('id'),
                                   json_response.get('name')))
        else:
            print("No result")
    except requests.HTTPError as e:
        if e.response.status_code == 400:
            print("Not a valid JSON")
        else:
            print("Error code:", e.response.status_code)
