#!/usr/bin/python3
"""def: say my name
    @first_name: 1 param
    @last_name: 2 param
    print the name and last name"""


def say_my_name(first_name, last_name=""):
    """valid the errors of first name and last name"""
    if type(first_name) is not str:
        """message error"""
        raise TypeError("first_name must be a string$")
    if type(last_name) is not str:
        """message error"""
        raise TypeError("last_name must be a string$")
    """valid if is none 1 or 2 param"""
    if first_name is None or last_name is None:
        first_name == last_name == ""
    """print the params"""
    print("My name is {} {}$".format(first_name, last_name))
