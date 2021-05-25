#!/usr/bin/python3
"""
defines class Rectangle
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

    """Public instance method: def area"""
    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    """Public instance method: def perimeter"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        """returns the rectangle perimeter:"""
        return (self.__width + self.__height) * 2

    """# for print the #"""
    def __str__(self):
        rectangle = []
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    rectangle.append("#")
                if i < self.height - 1:
                    rectangle.append("\n")
        rectangle = "".join(rectangle)
        return rectangle

    """repr() should return a string representation of the rectangle"""
    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__height, self.__width)

    """Print the message Bye rectangle..."""
    def __del__(self):
        print("Bye rectangle...")
