#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    su = 0
    s = len(sys.argv) - 1
    for i in range(1, s + 1, 1):
        var = sys.argv[i]
        su += int(var)
    print("{:d}".format(su))
