#!/usr/bin/python3
"""
Class Base : manage id propertyibute in
all your future classes and
to avoid duplicating the same code
(by extension, same bugs ;)
"""

import json
import os


class Base:
    """Base of all classes in this project"""

    __nb_objects = 0

    def __init__(self, _id=None):
        """Private propertyibutes and id fields are manipulated here
            Args:
                _id (int): must be of type integer
        """
        if _id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = _id

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string
        Returns a JSON representation of list_dictionaries.

        Args:
            list_dictionaries: list of dictonaries

        Returns: JSON representation of the list_directories
        """
        if list_dictionaries is None:
            list_dictionaries = []
        elif type(list_dictionaries) is not list:
            raise TypeError("list_dictionaries must be a list of dictionaries")

        for dictonary in list_dictionaries:
            if not isinstance(dictonary, dict):
                error_msg = "list_dictionaries must be a list of dictionaries"
                raise TypeError(error_msg)

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file
        writes the JSON string representation of
        list_objs to a file.

        Args:
            list_objs: list of instances who inherits Base
        """
        if list_objs is None:
            list_objs = []

        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as ready_file:
            ready_file.write((cls.to_json_string([c.to_dictionary()

                                                 for c in list_objs])))

    @staticmethod
    def from_json_string(json_string):
        """_from_json_string_
        returns the list of the JSON string
        representation json_string

        Args:
            json_string :a string representing
            a list of dictionaries
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """load_from_file

        Returns a list of instances.
        """
        filename = "{}.json".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        lst_inst = []
        with open(filename, "r", encoding="utf-8") as r:
            list_dicts = cls.from_json_string(r.read())
            lst_inst = [cls.create(**dictonary) for dictonary in list_dicts]
        return lst_inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save_to_file_csv
        Serializes list_objs in CSV format
        and saves it to a file.

        Args:
            list_objs: list of instances
        """
        if list_objs is None:
            list_objs = []

        filename = "{}.csv".format(cls.__name__)
        properties = ('id', 'size', 'width', 'height', 'x', 'y')
        with open(filename, "w", encoding="utf-8") as rf:
            for o in list_objs:
                dictonary = o.to_dictionary()
                list_ = []
                for property in properties:
                    if property not in dictonary:
                        continue
                    list_.append(str(dictonary.get(property)))
                rf.write(",".join(list_))
                rf.write("\n")

    @classmethod
    def load_from_file_csv(cls):
        """load_from_file_csv
        Deserializes CSV format from a file.

        Returns: list of instances
        """
        filename = "{}.csv".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        list_objs = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                arguments = line[:-1].split(",")
                o = cls(1, 1)
                o.update(*[int(x) for x in arguments])
                list_objs.append(o)
        return list_objs

    @classmethod
    def create(cls, **dictionary):
        """_create_instance
        Think of is as a special photocopy machine that
        prints instance and attributes thereof
        Returns an instance with all attributes already set.

        Args:
            dictionary: **kwargs

        Returns: instance created
        """
        dummy_instance = cls(1, 1)
        dummy_instance.x = 0
        dummy_instance.y = 0
        dummy_instance.update(**dictionary)
        return dummy_instance

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Launches a Turtle window and draws rectangles and squares.

        Args:
            list_rectangles: Rectangle instances
            list_squares: Square instances
        """
        # Import necessary modules and setup turtle
        import turtle
        import time
        from random import randrange

        _artwork = turtle.Turtle()
        _artwork.color("green")
        turtle.bgcolor("red")
        _artwork.shape("square")
        _artwork.pensize(8)

        # Loop through both lists and draw the shapes
        for _shape in (list_rectangles and list_squares):
            _artwork.penup()
            _artwork.setpos(0, 0)
            turtle.Screen().colormode(255)
            _artwork.pencolor((randrange(255), randrange(255), randrange(255)))
            # Call the helper method to draw the shape
            Base.draw(_artwork, _shape)
            time.sleep(1)
        time.sleep(5)
