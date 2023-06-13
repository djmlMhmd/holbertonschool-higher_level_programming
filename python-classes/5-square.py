#!/usr/bin/python3
"""Define new class:"""


class Square:
    """
    Class of square
    """
    def __init__(self, size=0):
        """
       New square with his size
        Args :
            size : Size of the square
        """
        self.__size = size

    def area(self):
        """
        Returns : area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Get the size of the square
        Returns:
            int: the size of the square
        """
        return self.size

    @size.setter
    def size(self, value):
        """
        Set the size of the square
        args:
            value : the size value to be set
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        Print a visual of the square.
        If the size is 0, print nothing.
        """
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
