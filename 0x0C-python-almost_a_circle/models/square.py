#!/usr/bin/python3
""" class Square that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class constructor """
    def __init__(self, size, x=0, y=0, id=None):
        """ Call the super class with id, x, y,
        width and height - this super call will use
        the logic of the __init__ of the Rectangle
        class. The width and height must be assigned
        to the value of size """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloading __str__ method should return
        [Square] (<id>) <x>/<y> - <size> - in our
        case, width or height"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)