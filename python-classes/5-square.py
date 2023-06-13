#!/usr/bin/python3
"""Define new class:"""


class Square:
    """Class of square"""
    def __init__(self, size=0):
        """New square with his size
        Args :
            size : Size of the square
        Raises:
            TypeError : If size not int
            ValueError : If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def area(self):
        """Returns : area of the square"""
        return self.__size ** 2
    
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size of the square.
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

        def my_print(self):
            """
            Print a visual of the square.
            If size 0 print nothing.
            """
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()