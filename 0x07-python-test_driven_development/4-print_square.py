#!/usr/bin/python3


def print_square(size):
        """if type of value if is integer"""
        if type(size) is not int:
            """print the error"""
            raise TypeError("size must be an integer")
        """if size is number negative"""
        if size < 0:
            """print the error"""
            raise ValueError("size must be >= 0")
        if size == 0 or size is None:
            print()
        else:
            for i in range(0, size):
                print("{}".format('#' * size))
