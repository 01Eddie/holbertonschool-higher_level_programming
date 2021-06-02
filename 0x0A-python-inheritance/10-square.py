#!/usr/bin/python3
"""class Rectangle inheriting from the last exercise"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ principal method """
    def __init__(self, size):
        """ The built-in super() function allows you to
        invoke a method of a parent class from a child class. """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    """ public instance method """
    def area(self):
        return self.__size ** 2
