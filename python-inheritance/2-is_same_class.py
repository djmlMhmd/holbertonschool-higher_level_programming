#!/usr/bin/python3
"""""the object is exactly an instance"""


def is_same_class(obj, a_class):
    """a function that returns True if the object is exactly
    an instance; otherwise False.
    """
    return type(obj) is a_class
