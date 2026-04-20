#!/usr/bin/python3
"""Sends a POST request with an email and displays the response body."""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("utf-8")

    req = urllib.request.Request(
        sys.argv[1],
        data=data,
        headers={"cfclearance": "true"}
    )

    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
