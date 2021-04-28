#!/usr/bin/python3
for i in range(ord('z'), ord('a') -1, -1):
    may = chr(i)
    if i%2 != 0:
        may = chr(i - 32)
    print("{}".format(may), end = '')
