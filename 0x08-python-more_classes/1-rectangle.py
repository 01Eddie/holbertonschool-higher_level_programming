#!/usr/bin/python3
"""
# Write a class Rectangle that defines a rectangle by:
(based on 0-rectangle.py)
#
# Private instance attribute: width:
# property def width(self): to retrieve it
# property setter def width(self, value): to set it:
# width must be an integer, otherwise raise a TypeError
exception with the message width must be an integer
# if width is less than 0, raise a ValueError exception
with the message width must be >= 0
# Private instance attribute: height:
# property def height(self): to retrieve it
# property setter def height(self, value): to set it:
# height must be an integer, otherwise raise a TypeError
exception with the message height must be an integer
# if height is less than 0, raise a ValueError exception
with the message height must be >= 0
# Instantiation with optional width and height:
def __init__(self, width=0, height=0):
# You are not allowed to import any module
"""


class Rectangle:
    """Define the variable or attribute in the principal method"""
    def __init__(self, width=0, height=0):
        """The __ define the attribute in private instance"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """property getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter method"""
        if value is None:
            raise TypeError("width must be an integer")

        """TypeError exception with the message width must be an integer"""
        if (type(value) is not int and type(value) is not float):
            raise TypeError("width must be an integer")

        """ValueError exception with the message width must be >= 0"""
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value
        return value

    @property
    def height(self):
        """property getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter method"""
        if value is None:
            raise TypeError("height must be an integer")

        """TypeError exception with the message height must be an integer"""
        if (type(value) is not int and type(value) is not float):
            raise TypeError("height must be an integer")
        """ValueError exception with the message height must be >= 0"""
        if (value <= 0):
            raise ValueError("height must be >= 0")
        self.__height = value
        return value
