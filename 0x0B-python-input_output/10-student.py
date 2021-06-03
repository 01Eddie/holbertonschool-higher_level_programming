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
    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            """ Otherwise, all attributes must be retrieved """
            new_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
                else:
                    pass
            return new_dict
