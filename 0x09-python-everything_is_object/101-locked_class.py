#!/usr/bin/python3
class LockedClass:
    """
    slots provide a static structure which prohibits
    additions after the creation of an instance.
    """
    __slots__ = ['first_name']
