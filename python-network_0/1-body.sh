#!/bin/bash
# aklsdfkalsdfalkj
res=$(curl -s -o /tmp/body -w "%{http_code}" "$1") [ "$res" -eq 200 ] && cat /tmp/body
