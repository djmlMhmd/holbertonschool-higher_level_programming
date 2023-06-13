#!/usr/bin/python3
"""Define new class:"""


class Square:
    """Class of square"""
    def __init__(self, size=0):
        """
        New square with his size
        Args :
            size : Size of the square
        """
        self.__size = size

    @property
    def size(self):
        """
        Returns the size of the square.
        
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets size of the square.
        Args:
            value : The new size of the square.
        Raises:
            TypeError: If value is not an int.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns : area of the square
        """
        return self.__size * self.__size
    