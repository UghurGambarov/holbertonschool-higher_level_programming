#!/usr/bin/python3
"""Sends a request and handles HTTP errors using status codes."""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url, headers={"cfclearance": "true"})

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
