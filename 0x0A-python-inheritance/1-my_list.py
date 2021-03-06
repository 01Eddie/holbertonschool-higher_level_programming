#!/usr/bin/python3
"""
Class MyList that inherits from list
    Public instance method: def print_sorted(self): that prints
    the list, but sorted (ascending sort)
"""


class MyList(list):
    """Principal Method"""
    def __init__(self):
        pass
    """Can assume that all the elements of the list will be of type int"""
    def print_sorted(self):
        """Print List ascending sort"""
        print(sorted(self))
