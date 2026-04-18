#!/bin/bash
# asdfkjalskdfja;lskdjfl
res=$(curl -s -w "%{http_code}" "$1") [ "${res: -3}" -eq 200 ] && echo "${res::-3}"
