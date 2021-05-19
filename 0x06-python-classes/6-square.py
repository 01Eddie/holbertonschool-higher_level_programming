#!/usr/bin/python3
""" define or write class Square"""


class Square:
    """Define the variable or attribute in the principal method"""
    def __init__(self, size=0, position=(0, 0)):
        """The __ define the attribute in private instance"""
        self.__size = size
        self.__position = position

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
            x = self.__position[0]
            y = self.__position[1]
            for i in range(y):
                print("")

            for row in range(0, self.__size):
                for j in range(x):
                    print(" ", end="")
                for col in range(self.size):
                    print("#", end="")
                print()

    def position(self):
        return self.__position

    def position(self, value):
        if (type(value) is not tuple or len(value) != 2) or (
            value[0] is not int or value[0] < 0) or (
                type(value[1]) is not int or type(value[1]) < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value[:]
