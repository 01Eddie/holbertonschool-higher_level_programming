#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newL = my_list[:]
    j = 0
    for i in range(0, len(my_list), 1):
        if my_list[i] == search:
            newL[j] = replace
        j += 1
    return newL
