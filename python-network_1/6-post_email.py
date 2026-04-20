#!/usr/bin/python3
"""Sends a POST request with an email and displays the response body."""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email_value = sys.argv[2]

    response = requests.post(
        url,
        data={"email": email_value},
        headers={"cfclearance": "true"}
    )

    print(response.text)
