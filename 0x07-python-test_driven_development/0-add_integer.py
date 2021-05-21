#!/usr/bin/python3
"""def: add integer
    @a: 1 param
    @b: 2 param
    return a or b """


def add_integer(a, b=98):
    """valid the first param if is none"""
    if a is None:
        """print error"""
        raise TypeError("a must be an integer")
    """valid the first param if not integer"""
    if type(a) is not int and type(a) is not float:
        """print error"""
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        """print error"""
        raise TypeError("b must be an integer")
    """return a and b forcing integer"""
    return int(a) + int(b)
