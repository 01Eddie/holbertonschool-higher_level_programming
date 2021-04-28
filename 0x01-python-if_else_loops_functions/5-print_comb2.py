#!/usr/bin/python3
for i in range(0, 100, 1):
    if i == 99:
        print("{:d}".format(i), end = ' \n')
    elif i < 10:
        print("0{:d}".format(i), end = ', ')
    else:
        print("{:d}".format(i), end = ', ')
