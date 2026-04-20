#!/bin/bash
# Sends a GET request to a URL and displays the body only if the response status is 200
curl -s -w "%{http_code}" "$1" | sed -e '/200$/!d' -e 's/[0-9]\{3\}$//'
