#!/usr/bin/python3
"""lookup(obj)
a function that returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """Method to check all attributes of
    an object.

    Args:
        obj: object to look into

    Return :
         list of available attributes and methods of an object
    """

    return dir(obj)
