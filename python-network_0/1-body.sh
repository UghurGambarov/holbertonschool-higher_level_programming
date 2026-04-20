#!/bin/bash
# Sends a GET request to a URL and displays the body only if the response status is 200
curl -s -o /tmp/body -w "%{http_code}" "$1" | grep -q "200" && cat /tmp/body
