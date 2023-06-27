#!/usr/bin/python3
"""
module that writes  constructs
a class Square with size validation
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
