#!/usr/bin/python3
"""
module that writes  constructs
a class Square with size validation and
area culculation.
"""


class Square:
    """
    module that writes  constructs
    a class Square with size validation

    Attributes:
        size (int): size field of type int in the Square class.
    """
    def __init__(self, size=0):
        """
        This initializes the class and sets the size  attribute
        to the suplied int from arguments

        This size attribute is a Private instance of the class
        Square and should always be greater than 0.


        Args:
            size (int): the requires parameter.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        This Public instance method:
        def area(self):
        that returns the current square area.

        Retrieves Private instance attribute: size

        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        property def size(self):
        to retrieve Private instance attribute: size

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        property setter def size(self, value):
        to set Private instance attribute: size

        args:

        value

        the int to set as new_size .
        This updated the Private instance attribute: size
        with new int.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
