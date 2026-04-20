#!/usr/bin/python3
"""Takes a URL, sends a request, and displays X-Request-Id header value."""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url, headers={"cfclearance": "true"})
    print(response.headers.get("X-Request-Id"))
