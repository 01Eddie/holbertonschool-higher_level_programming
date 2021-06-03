#!/usr/bin/python3
"""Function that creates an Object from a “JSON file"""

import json


def load_from_json_file(filename):
    """The with statement Deserialize fp (a .read()
    -supporting file-like object containing a JSON
    document) to a Python object."""
    with open(filename, 'r', encoding="UTF-8") as file:
        return json.load(file)
