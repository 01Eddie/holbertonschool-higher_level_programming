#!/usr/bin/python3
"""def: text_indentation
    @text: param
    print text"""
def text_indentation(text):
    """compare if isn't string"""
    if type(text) is not str:
        """message of error"""
        raise TypeError("text must be a string")
    print("{}".format(text))