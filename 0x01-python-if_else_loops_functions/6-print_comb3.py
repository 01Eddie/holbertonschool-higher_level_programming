#!/usr/bin/python3
for i in range(0, 10, 1):
    for j in range(i + 1, 10, 1):
        if (i == 8 and j == 9):
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d}".format(i, j), end=', ')
