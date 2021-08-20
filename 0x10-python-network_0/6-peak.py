#!/usr/bin/python3


def find_peak(list_of_integers):

    sizeArr = len(list_of_integers) - 1
    index = 0
    middle = sizeArr
    if sizeArr == -1:
        return None
    while (index < sizeArr):
        middle = (index + sizeArr) // 2
        if list_of_integers[middle] < list_of_integers[middle + 1]:
            index = middle + 1
        else:
            sizeArr = middle
    return list_of_integers[index]