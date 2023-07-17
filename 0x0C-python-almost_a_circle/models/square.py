#!/usr/bin/python3
"""square module.
Inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square.
    Inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """a Square instance.

        Args:
            __size: size
            __x: position
            __y: position
            id: id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of a square"""
        sha_ = "[{}] ({}) ".format(self.__class__.__name__, self.id)
        _pe = "{}/{} - {}".format(self.x, self.y, self.width)
        return sha_ + _pe

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """_update_
        Updates instance properties.

        Args:
            id property
            size property
            x property
            y property
        """
        if args and len(args) != 0:
            for count in range(len(args)):
                if count == 0:
                    if args[count] is None:
                        self.__init__(
                                self.width, self.width, self.x, self.y)
                    else:
                        self.id = args[count]
                if count == 1:
                    self.width = args[count]
                    self.height = args[count]
                if count == 2:
                    self.x = args[count]
                if count == 3:
                    self.y = args[count]
        else:
            if kwargs and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        if value is None:
                            self.__init__(
                                    self.width, self.width, self.x, self.y)
                        else:
                            self.id = value
                    elif key == "size":
                        self.width = value
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

    def to_dictionary(self):
        """returns dictionary representation
        of a square"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
