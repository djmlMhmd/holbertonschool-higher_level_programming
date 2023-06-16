#!/usr/bin/python3
"""
Class that represents a rectangle.
"""


class Rectangle:
    """
        Representing a rectangle.
        Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
    def __init__(self, width=0, height=0):
        """
        Initialize  rectangle instance with optional width and height.
        Args:
            width (int): The width rectangle (default: 0).
            height (int): The height rectangle (default: 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Method for width attribute.
        Returns: The width rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.
        Args:
            value (int): The width value to set.
        Raise:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.
        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Method for the height attribute.
        Args:
            value (int): The height value to set.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        """
        print the rectangle with the character #
        """
        rectangle_str = ""
        if self.width == 0 or self.height == 0:
            return rectangle_str
        for i in range(self.height):
            rectangle_str += ("#" * self.width) + "\n"
        return rectangle_str[:-1]
    
    def __repr__(self):
        """
        Returns: returns a string representation rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
    
    def __del__(self):
        """
        Print the message, when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
