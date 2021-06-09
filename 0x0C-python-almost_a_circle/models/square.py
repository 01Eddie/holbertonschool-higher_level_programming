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
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ The setter should assign (in this order)
        the width and the height - with the same value """
        return self.width

    @size.setter
    def size(self, value):
        """setter should have the same value
        validation as the Rectangle for width and height"""
        self.width = value
        self.height = value
        return value

    def update(self, *args, **kwargs):
        if len(args) > 0:
            """ defino el array que va a recorrer """
            array = ["id", "size", "x", "y"]

            for i, arg in enumerate(args):
                """ setattribute hara que tome el objeto de la instancia con el array
                y hara a que se iguale """
                setattr(self, array[i], args[i])
        else:
            """ **kwargs must be skipped if *args exists and is not empty """
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """adding the public method def to_dictionary
        (self): that returns the dictionary
        representation of a Square:"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
