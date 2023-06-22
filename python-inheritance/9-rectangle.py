#!/usr/bin/python3
"""Create class BaseGeometry"""


class BaseGeometry:
    def area(self):
        return self.__width * self.__height
    
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
        super().__init__()
        self.width = 0
        self.height = 0
        self.width = width
        self.height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"