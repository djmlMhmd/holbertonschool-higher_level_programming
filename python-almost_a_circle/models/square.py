#!/usr/bin/python3
"""Square Base"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, width, height)
