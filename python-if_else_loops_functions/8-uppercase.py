#!/usr/bin/env python3
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            result += "{}".format(chr(ord(char) - 32))
        else:
            result += "{}".format(char)
    print("{}".format(result))
