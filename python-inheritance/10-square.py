#!/usr/bin/python3
"""class Square from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square, subclass rectangle
    """
    def __init__(self, size):
        """Instantiation rectangle function"""
        super().integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Return rectangle, square"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Return area square"""
        return self.__size ** 2
