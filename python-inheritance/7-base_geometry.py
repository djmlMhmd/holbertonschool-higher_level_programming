#!/usr/bin/python3
"""Create class BaseGeometry"""


class BaseGeometry():
    """Class BaseGeometry"""
    def area(self):
        """Raise an Exception with a message"""
        raise NotImplementedError("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
