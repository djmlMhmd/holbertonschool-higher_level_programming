#!/usr/bin/python3
"""Create class BaseGeometry"""


class BaseGeometry:
    def area(self):
        raise NotImplementedError("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")

class Rectangle(BaseGeometry):
    """Class Rectangle, subclass of BaseGeometry

    comments:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """
    def __init__(self, width, height):
        """Using BaseGeometry(superclass) function"""
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
