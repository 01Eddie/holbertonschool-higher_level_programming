#!/usr/bin/python3
""" define or write class Square"""


class Square:
    """Define the variable or attribute in the principal method"""
    def __init__(self, size=0):
        """if type of size if is integer"""
        if type(size) is not int:
            """print the error"""
            raise TypeError("size must be an integer")
        """if size is number negative"""
        if size < 0:
            """print the error"""
            raise ValueError("size must be >= 0")
        """The __ define the attribute in private instance"""
        self.__size = size
