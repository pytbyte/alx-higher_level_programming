#!/usr/bin/python3
"""
Class Base : manage id properties in
all your future classes and
to avoid duplicating the same code
(by extension, same bugs ;)
"""


class Rectangle:
    """
    class rectangle inherits
    from base
    """
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """_Rectangle instance_
        class rectangle inherits from base

        Args:
            width (_int_): width instance properties
            height (_int_): height instance properties
            x: point
            y: point
            id: int id
        """
 
 
        self.height = height
        self.width = width
        self.y = y
        self.x = x        
        super().__init__(id)
    
    @property
    def height(self):
        """Access height properties"""
        return self.__height
    
    @property
    def width(self):
        """Access width properties"""
        return self.__width
    
    @property
    def x(self):
        """Access x properties"""
        return self.__x
    
    @property
    def y(self):
        """Access y properties"""
        return self.__y
    
    @height.setter
    def height(self, value):
        """ assigns value to height properties"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
           raise ValueError("height must be > 0")
        self.__height = value
    
    @width.setter
    def width(self, value):
        """ assigns value to width properties"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
           raise ValueError("width must be > 0")
        self.__width = value

    @y.setter
    def y(self, value):
        """ assigns value to height properties"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
           raise ValueError("y must be >= 0")
        self.__y = value

    @x.setter
    def x(self, value):
        """ assigns value to height properties"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
           raise ValueError("x must be >= 0")
        self.__x = value

    
    def area(self):
        """culculate the area of rectangle"""
        return (self.__height * self.__width)
    
    def display(self):        
        """Prints the Rectangle instancefilled with #."""

        for _ in range(self.__y):
            print()

        lines = [" " * self.__x + "#" * self.__width for _ in range(self.__height)]
        print("\n".join(lines))

    def __str__(self):
        """
        return a string representation of the rectangle
        """
        shape = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return shape
    
    
    