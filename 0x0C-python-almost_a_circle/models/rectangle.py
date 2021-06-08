#!/usr/bin/python3
""" Import class from Base """
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        return value

    @property
    def height(self):
        """ get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
        return value

    @property
    def x(self):
        """ get x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
        return value

    @property
    def y(self):
        """ get y """
        return self.__y

    @y.setter
    def y(self, value):
        """ set y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
        return value

    def area(self):
        """ Area of rectangle """
        return self.width * self.height
    
    def display(self):
        """ Function of display """
        simbol = '#'
        if self.x == 0 or self.y == 0:
            print("")
        for i in range(0, self.height):
            for j in range(0, self.width):
                print("{}".format(simbol), end="")
            if i < self.x - 1:
                print(" ", end="") 
            print("")
    def __str__(self):
        """ it returns [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        if self.width is None or self.height is None or self.x is None or self.y is None:
            self.width = 0
            self.height = 0
            self.x  = 0
            self.y  = 0
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height) 
