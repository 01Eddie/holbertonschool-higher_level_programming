#!/usr/bin/python3
"""Function that writes a string to a text file (UTF8)
and returns the number of characters"""


def write_file(filename="", text=""):
    """ the with statement """
    with open(filename, 'w', encoding='utf8') as f:
        v = f.write(text)
        f.close()
        return v
