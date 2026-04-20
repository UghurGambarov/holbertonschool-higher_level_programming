#!/bin/bash
# Sends a GET request to a URL and displays the body only if the response status is 200
curl -sL "$1" -w "%{http_code}" | sed -e '$!b' -e 's/200$//' -e 't' -e 'd'
