#!/usr/bin/python3
"""
9-rectangle.
Creates a Rectangle class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class rectangle
    """

    def __init__(self, width, height):
        """
        creates an instance.

        Args:
            - width: width of the rectangle
            - heigth: height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a priety string.
        """

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """
        area culculations to go here
        """

        return self.__width * self.__height
