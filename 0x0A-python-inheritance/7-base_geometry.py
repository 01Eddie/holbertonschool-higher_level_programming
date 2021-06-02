#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """principal function"""
    def __init__(self):
        pass
        
    """public method def area"""
    def area(self):
        """error Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Value is not an integer: raise a TypeError
        exception, with the message <name> must be
        an integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        """
        Value is less or equal to 0: raise a
        ValueError exception with the message <name>
        must be greater than 0
        """
        if value <= 0:    
            raise ValueError("{} must be greater than 0".format(name))
        return (name, value)
