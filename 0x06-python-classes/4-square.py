#!/usr/bin/python3
""" define or write class Square"""


class Square:
    """Define the variable or attribute in the principal method"""
    def __init__(self, size=0):
        """The __ define the attribute in private instance"""
        self.__size = size

    @property
    def size(self):
        """property getter method"""
        """Here retrieve the variable size with a new value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter method"""
        """if type of value if is integer"""
        if type(value) is not int:
            """print the error"""
            raise TypeError("size must be an integer")
        """if size is number negative"""
        if value < 0:
            """print the error"""
            raise ValueError("size must be >= 0")
        self.__size = value

    """Instanced public method for return square area"""
    def area(self):
        """Here do the square area"""
        return self.__size ** 2
