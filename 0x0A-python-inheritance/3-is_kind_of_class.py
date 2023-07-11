#!/usr/bin/python3
"""3-is_kind_of_class.
checks f the object is an instance of,
or if the object is an instance of a class
that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    checks f the object is an instance of,
    or if the object is an instance of a class
    that inherited from, the specified class

    Args:
        obj: target object
        a_class: specified class to check

    Returns: True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
