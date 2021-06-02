#!/usr/bin/python3
"""class Square inheriting from the last exercise"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ principal class """
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    """public method def area"""
    def area(self):
        return self.__size ** 2

    """public method magic"""
    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
