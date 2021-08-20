#!/usr/bin/python3
""" Find_peak: function that find peak"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    list_of_integers.sort()
    for i in range(len(list_of_integers)):
        return list_of_integers[i-1]
        