#!/usr/bin/python3

"""
    Args:
        a (int):  integers or floats
        b (int):  integers or floats
"""

def add_integer(a, b=98):
    """Function that add two integers or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int,float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
