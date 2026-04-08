#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = f"Last digit of {number} is {str(number)[-1]} and is "
if str(number)[-1] > 5:
    a += "greater than 5"
elif str(number)[-1] == 0:
    a += "0"
else:
    a += "less than 6 and not 0"
print(a)
