#!/usr/bin/python3
"""
10-student.
Creates a Student class.
"""


class Student:
    """Class student.
    Public attributes:
        - first_name
        - last_name
        - age

    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation
        of a Student instance.
        Args:
            - attrs: list of attributes
        Return: the dict representation of the instance.
        """

        json_data = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    json_data.update({x: self.__dict__[x]})
            return json_data
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance.
        Args:
            json: dictionnary properties
        """

        for x in json:
            self.__dict__.update({x: json[x]})
