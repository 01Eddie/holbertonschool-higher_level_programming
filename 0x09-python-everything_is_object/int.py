#!/usr/bin/python3
def __init__(self):
    a = 1024
    b = 1024
    del a
    del b
    c = 1024
import dis
dis.dis(__init__)