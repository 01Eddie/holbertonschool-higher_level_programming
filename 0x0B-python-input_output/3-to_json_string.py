#!/usr/bin/python3
import json
"""Function that returns the JSON representation of an object (string)"""


def to_json_string(my_obj):
    """printing initial json"""
    initialization_string = json.dumps(my_obj)
    return initialization_string
