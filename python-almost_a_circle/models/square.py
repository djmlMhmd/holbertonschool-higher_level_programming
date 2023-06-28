#!/usr/bin/python3
"""Square Base"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assigns an argument"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        else:
                for key, value in kwargs.items():
                    """assigns a value to an object attribute"""
                    setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representing rectangle"""
        return {
            'id': self.id, 
            'size': self.width,
            'x': self.y,
            'y': self.x
        }
