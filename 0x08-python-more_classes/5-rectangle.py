#!/usr/bin/python3
"""Rectangle Class.

Empty class that defines a rectangle.

Usage Sample:

    Rectangle = __import__('0-rectangle').Rectangle

    my_rectangle = Rectangle()
    print(type(my_rectangle))
    print(my_rectangle.__dict__)
"""


class Rectangle:
    """
        A method that creates the object rectangle.

        creates an instance of the Rectangle object
        with width and height.

        Args:
            width: default value of 0.
            height: default value of 0.
    """

    def __init__(self, width=0, height=0):
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
        """int: width"""
        return self.__width

    @property
    def height(self):
        """int: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Args:
           value (int): int
        Raises:
            TypeError: not int
            ValueError: less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """
        Args:
            value (int): int
            Raises:
                TypeError: not int
                ValueError: less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        Area calculator

        Return:
            int: area
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Perimeter calculator

        Return:
            int: perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.height) * 2

    def __str__(self):
        """
        should fill the rectangle area with the character #
        returns the rectangle area
        """
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for i in range(self.__height):
            rectangle += "#" * self.__width
            if i != (self.__height - 1):
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """
        return a string representation of the rectangle
        to use in  recreating a new instance by using eval()
        """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints after xecution"""

        print("Bye rectangle...")
