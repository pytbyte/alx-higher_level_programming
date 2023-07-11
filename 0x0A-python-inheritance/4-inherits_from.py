#!/usr/bin/python3
"""4-inherits_from
returns True if the object is an instance
of a class that inherited (directly or indirectly)
from the specified class
"""


def inherits_from(obj, a_class):
    """4-inherits_from.
       returns True if the object is an instance
       of a class that inherited (directly or indirectly)
       from the specified class


    Args:
       obj: target object
       a_class: specified class to check

    Returns: True or False
    """
    return isinstance(type(obj), a_class) and type(obj) != a_class
