#!/usr/bin/python3


def find_peak(list_of_integers):
    list_of_integers.sort()
    for i in range(len(list_of_integers)):
        return list_of_integers[i-1]
