#!/usr/bin/python3
""" Class Base: """
import json


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
            return []
        return json.dumps(list_dictionaries)

    @staticmethod
    def save_to_file(cls, list_objs):
        """class method def save_to_file(cls, list_objs):
        that writes the JSON string representation
        of list_objs to a file: (PREGUNTAR POR LA FUNCION POR Q NO ME SALE)"""
        filename = cls.__name__ + ".json"
        represList = []

        if list_objs is not None:
            for i in list_objs:
                represList.append(cls.to_dictionary(i))
        else:
            """If list_objs is None, save an empty list"""
            """You must overwrite the file if it already exists"""
            with open(filename, 'w', encoding="utf-8") as myfn:
                """You must use the static method to_json_string"""
                myfn.write(cls.to_json_string(represList))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            return json.loads(json_string)