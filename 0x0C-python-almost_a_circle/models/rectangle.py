#!/usr/bin/python3
"""
class rectangle inherits
from base
"""
from models.base import Base


class Rectangle(Base):
    """
    class rectangle inherits
    from base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle instance
           inherits from base

        Args:
            width (_int_): width instance property
            height (_int_): height instance properties
            x: point
            y: point
            id: int id
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """access width"""
        return self.__width

    @width.setter
    def width(self, value):
        """assigner for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """access for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """assign to height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """culculate the area of rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the Rectangle instancefilled with #."""
        for lines in range(self.y):
            print("")
        for j in range(self.height):
            for k in range(self.width + self.x):
                if k < self.x:
                    print(" ", end="")
                else:
                    print("#", end="")
            print("")

    def __str__(self):
        """string representation of rectangle"""
        sha_ = "[{}] ({}) ".format(self.__class__.__name__, self.id)
        _pe = "{}/{} - {}/{}".format(
                self.x, self.y, self.width, self.height)
        return sha_ + _pe

    def update(self, *args, **kwargs):
        """Updates propertys of an instance.

        Args:
            id property
            width property
            height property
            x property
            y property
        """
        if args or len(args) != 0:
            for count in range(len(args)):
                if count == 0:
                    if args[count] is None:
                        self.__init__(
                                self.width, self.height, self.x, self.y)
                    else:
                        self.id = args[count]
                if count == 1:
                    self.width = args[count]
                if count == 2:
                    self.height = args[count]
                if count == 3:
                    self.x = args[count]
                if count == 4:
                    self.y = args[count]
        else:
            if kwargs or len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        if value is None:
                            self.__init__(
                                    self.width, self.height, self.x, self.y)
                        else:
                            self.id = value
                    if key == "width":
                        self.width = value
                    if key == "height":
                        self.height = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value

    def to_dictionary(self):
        """returns dictionary representation
        of rectangle"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
