#!/usr/bin/python3
from os import error
import sys
"""Using my previous functions"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

add_item = sys.argv
"""pop: remove and return item at index (default last)"""
add_item.pop(0)
try:
    """The list must be saved as a JSON
    representation in a file named add_item.json
    - If the file doesn’t exist, it should be
    created"""
    with open('add_item.json', 'x') as f:
        save_to_json_file(add_item, "add_item.json")
except:
    listNew = load_from_json_file("add_item.json")
    save_to_json_file(listNew + add_item, "add_item.json")
