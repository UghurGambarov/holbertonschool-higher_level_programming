#!/usr/bin/python3
"""Sends a request to a URL and displays the X-Request-Id from the response."""
import urllib.request
import sys


if __name__ == "__main__":
    req = urllib.request.Request(
        sys.argv[1],
        headers={"cfclearance": "true"}
    )
    with urllib.request.urlopen(req) as response:
        print(response.headers.get("X-Request-Id"))
