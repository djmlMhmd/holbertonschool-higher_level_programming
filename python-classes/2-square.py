#!/usr/bin/python3
"""Define new class:"""


class Square:
    """Class of square"""
    def __init__(self, size=0):
        """New square with his size"""
        if not isinstance:
            raise TypeError
        elif size < 0:
            raise ValueError
        else:
            self.__size = size
