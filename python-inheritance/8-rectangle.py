#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        raise NotImplementedError("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().__init__()
        self.width = 0
        self.height = 0
        self.width = width
        self.height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
