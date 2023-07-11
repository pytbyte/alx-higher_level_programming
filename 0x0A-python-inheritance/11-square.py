#!/usr/bin/python3
"""
module cith class square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class square with rectangle attributes
    """
    def __init__(self, size):
        """
        creates square assigning attributes
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        area inherited from area.
        """
        return super().area()

    def __str__(self):
        """
        priety representation of the square
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
