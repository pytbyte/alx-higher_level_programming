#!/usr/bin/python3
"""
module that constructs
a class Square with attribute position
"""


class Square:
    """
    module that constructs
    a class Square with attribute position

    Attributes:
        size (int): integer greater than 0.
        position (tuple): Tuple with x and y
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        position:
        property def position(self):
        to retrieve Private instance attribute: position

        Args:
            size (int): parameter value for size
            position (tuple): Tuple with set of 2 ints
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if (not isinstance(position, tuple) or len(position) != 2
            or not isinstance(position[0], int) or
            not isinstance(position[1], int) or position[0] < 0
                or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
        """
        Private instance attribute: size
        """
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

    def my_print(self):
        """
        Public instance method: def my_print(self):
        prints in stdout the square with the character #:

        if size is equal to 0, print an empty line
        position should be use by using space
        Don’t fill lines by spaces when position[1] > 0
        """
        if self.__size == 0:
            print("")
        else:
            string_to_print = ""
            for i in range(self.position[1]):
                string_to_print += "\n"
            for x in range(self.size):
                for y in range(self.position[0]):
                    string_to_print += " "
                for z in range(self.size):
                    string_to_print += "#"
                string_to_print += "\n"
            print("{}".format(string_to_print), end='')

    @property
    def position(self):
        """
        property def position(self):
        to retrieve Private instance attribute: position

        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        property setter def property(self, value):
        to set Private instance attribute: property

        args:

        value

        must be a tuple of 2 positive integers, otherwise raise a TypeError
        exception.

        """
        if (not isinstance(value, tuple) or len(value) != 2 or not
            isinstance(value[0], int) or not isinstance(value[1], int)
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value