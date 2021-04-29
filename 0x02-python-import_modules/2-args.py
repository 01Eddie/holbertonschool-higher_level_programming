#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    s = len(sys.argv) - 1
    if s == 0:
        print("0 arguments.")
    elif s == 1:
        print("{} argument:".format(s))
    else:
        print("{} arguments:".format(s))
    for i in range(1, s + 1, 1):
        print("{}: {}".format(i, sys.argv[i]))
