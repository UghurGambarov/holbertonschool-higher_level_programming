#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if int(value) == value:
            print("{:d}".format(value))
    except:
        print("{} is not an integer".format(value))
