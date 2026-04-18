#!/bin/bash
# Send request and display size of response body in bytes
curl -s -o /dev/null -w "%{size_download}\n" "$1"
