#!/usr/bin/python3
"""Create class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle, subclass of BaseGeometry

    comments:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """
    def __init__(self, width, height):
        """Using BaseGeometry function"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
