#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    val = list(a_dictionary.values())
    key = list(a_dictionary.keys())
    if key is None or val is None:
        return None
    return key[val.index(max(val))]
