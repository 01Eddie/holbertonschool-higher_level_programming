#!/usr/bin/python3
def print_last_digit(number):
    val = number % 10
    if number < 0:
        val = -number % 10
        print("{:d}".format(val), end='')
    else:
        print("{:d}".format(val), end='')
    return val
