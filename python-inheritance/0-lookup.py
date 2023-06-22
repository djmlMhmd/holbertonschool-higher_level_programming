#!/usr/bin/python3
"""
Function that return the list
"""

def lookup(obj):
    """
    Returns: the list of available attributes
    """
    my_list = dir(obj)
    return dir(my_list)
