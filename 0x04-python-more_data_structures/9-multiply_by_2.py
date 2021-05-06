#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for itm, val in new_dictionary.items():
        new_dictionary[itm] = val*2
    return new_dictionary
