#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

"""if the last digit is greater than 5: the string and is greater than 5
if the last digit is 0: the string and is 0
if the last digit is less than 6 and not 0: the string and is less than 6 and not 0"""

digit = number % 10

if digit > 5:
    print("Last digit of {:d} is {:d} greater than 5".format(number, digit))
elif digit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, digit))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, digit))
