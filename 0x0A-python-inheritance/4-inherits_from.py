#!/usr/bin/python3
"""
Function that returns True if the object is an
instance of a class that inherited (directly or
indirectly) from the specified class ; otherwise
False
"""


def inherits_from(obj, a_class):
    """
    if the object is an instance of a class that
    inherited (directly or indirectly) from the
    specified class
    """
    if isinstance(obj, a_class) and not issubclass(a_class, type(obj)):
        return True
    else:
        return False
