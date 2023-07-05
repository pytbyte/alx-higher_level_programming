#!/usr/bin/python3

"""Rectangle Class.
creates an empty class that defines a rectangle.

Usage sample:

    Rectangle = __import__('0-rectangle').Rectangle

    my_rectangle = Rectangle()
    print(type(my_rectangle))
    print(my_rectangle.__dict__)
"""


class Rectangle:
    """Defines the structure of a rectangle.
    Args:
        width: width of the rectangle object as Integer.
        height: height of the rectangle object as integer.

    Attributes:
        width: width of the rectangle object as Integer.
        height: height of the rectangle object as integer.
    """

    def __init__(self, width=0, height=0):
        """A method that creates the Object.

        Initiatilizes object Rectangle with width and height.

        Args:
            width: default value of 0.
            height: default value of 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Accesses the width private attribute value.

        Returns:
            The width private attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width private attribute value.

        Arg:
            value: value to be set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Accesses the height private attribute value.

        Returns:
            The height private attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height private attribute value.

        Arg:
            value: the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
