#!/usr/bin/python3
""" Class Base: """
import json
from os import path


class Base:
    """ private class attribute __nb_objects = 0 """
    __nb_objects = 0
    """  class constructor """
    def __init__(self, id=None):
        """ if id is not None, assign the public
        instance attribute id with this argument
        value - you can assume id is an integer and
        you don’t need to test the type of it """
        if id is not None:
            """pide at.. publico"""
            self.id = id
        else:
            """ otherwise, increment __nb_objects
            and assign the new value to the public
            instance attribute id """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def save_to_file(cls, list_objs):
        """class method def save_to_file(cls, list_objs):
        that writes the JSON string representation
        of list_objs to a file:"""
        filename = cls.__name__ + ".json"

        if list_objs is not None:
                list_objs = [i.to_dictionary() for i in list_objs]
                
        """If list_objs is None, save an empty list"""
        """You must overwrite the file if it already exists"""
        with open(filename, 'w', encoding="utf-8") as myfn:
            """You must use the static method to_json_string"""
            myfn.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """the static method def from_json_string
        (json_string): that returns the list of the
        JSON string representation json_string:"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """the class method def create(cls, **dictionary):
        that returns an instance with all attributes already set:
            - **dictionary can be thought of as double pointer to a dictionary
            - To use the update method to assign all
        attributes, you must create a “dummy” instance before:
                - Create a Rectangle
                or Square instance with
                “dummy” mandatory attributes (width, height, size, etc.)
                - Call update instance method
                to this “dummy” instance to apply
                your real values
            - You must use the method def update(self, *args, **kwargs)
            - **dictionary must be used as **kwargs of the method update"""
        if cls.__name__ == 'Rectangle':
            dummyNew = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummyNew = cls(1, 0)
        dummyNew.update(**dictionary)
        return dummyNew

    @classmethod
    def load_from_file(cls):
        """the class method def load_from_file(cls):
        that returns a list of instances"""
        filename = cls.__name__ + ".json"
        instanceList = []
        """ If the file doesn’t exist, return an empty list """
        if path.exists(filename) is None or path.exists(filename) is False:
            return []
        else:
            """ Otherwise, return a list of instances - the type of these instances
            depends on cls (current class using this method) """
            with open(filename, 'r', encoding="utf-8") as myfn:
                f = myfn.read()
                myList = cls.from_json_string(f)
            """i = dict - el recorrido"""
            for i in myList:
                instanceList.append(cls.create(**dict))
            return instanceList
