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
    structure of a rectangle.

    Attribute:
        width: must be type int.
        height:  must be type int.
        number_of_instances: number of instance launched
        print_symbol: symbol "#" used in priety_rectanle printing

    """
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        A method that creates the object rectangle.

        creates an instance of the Rectangle object
        with width and height.

        Args:
            width: default value of 0.
            height: default value of 0.
        """
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        should fill the rectangle area with the character #
        returns the rectangle area
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        priety_rectangle = ""
        for x in range(self.__height):
            for y in range(self.__width):
                priety_rectangle += self.print_symbol
            priety_rectangle += "\n"
        return priety_rectangle[:-1]

    def __repr__(self):
        """
        return a string representation of the rectangle
        to use in  recreating a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del___(self):
        """
        module delete self

        deletes instance
        prints a message as return value
        decreases instance count per instance kill
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """
         Access the value of private attribute width.

        Returns:
            The width private attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value into private attribute width.

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
        Gets the value of private attribute height.

        Returns:
            The height private attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the value of private attribute height.


        Arg:
            value: value to be set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        A public object method.

        Returns:
            rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        A public object method.

        Returns:
            rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds the biggest Rectangle based on the area.

        Args:
            rect_1: Rectangle instance
            rect_2: Rectangle instance different from rect_1

        Returns:
            The instance with the biggest area,
            or rect_1 if both rectangles have the same area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance with width == height == size.

        Args:
            size: size to be assigned to new rectangle instance

        Returns:
            The new Rectangle instance
        """
        return cls(size, size)
