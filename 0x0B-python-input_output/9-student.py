#!/usr/bin/python3
"""class student that defines a student"""


class Student:
    """Principal function"""
    def __init__(self, first_name, last_name, age):
        """ Public instance attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """ Public method  """
    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return self.__dict__
