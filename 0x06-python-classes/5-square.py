#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """property getter method"""
        """Here retrieve the variable size with a new value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method"""
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

    def area(self):
        """public instance method"""
        return self.__size ** 2

    def my_print(self):
        """public instance method"""
        if self.__size == 0 or None:
            print()
        else:
            for i in range(0, self.__size):
                print("{}".format('#' * self.__size))
