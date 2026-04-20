#!/usr/bin/python3
"""Uses GitHub API with Basic Auth to display user ID."""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    response = requests.get(
        "https://api.github.com/user",
        auth=(username, token)
    )

    try:
        print(response.json().get("id"))
    except ValueError:
        print("None")
