#!/usr/bin/python3
"""
Script that uses Basic Authentication with a personal
access token to access the GitHub API
and display the user id.
"""


import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    access_token = sys.argv[2]

    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, access_token))
        response.raise_for_status()

        user_data = response.json()
        user_id = user_data.get('id')

        print(user_id)
    except requests.HTTPError as e:
        print("None")
