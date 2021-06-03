#!/usr/bin/python3
"""Function that writes an Object to a text file,
using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """The with statement and the parse a json"""
    with open(filename, 'w', encoding="UTF-8") as f:
        v = f.write(json.dumps(my_obj))
        f.close()
        return v
