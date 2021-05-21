def text_indentation(text):
    if type(text) is not str :
        raise TypeError("text must be a string")
    print("{}".format(text))