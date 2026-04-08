#!/usr/bin/python3
for i in range(97, 123):
    if "{:c}" != "e" or "{:c}" != "q":
        print("{:c}".format(i), end="")
    else:
        continue
