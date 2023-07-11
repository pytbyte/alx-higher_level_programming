#!/usr/bin/python3
"""2-is_same_class.
Finds if an object is exactly an instance of a  specified class.
"""


def is_same_class(obj, a_class):
    """2-is_same_class.
       Finds if an object is exactly an instance
       of a  specified class.
    Args:
        - obj: targte object 
        - a_class: specified class to verify the instance of

    Returns: True if obj is an instance of a_class,
    False otherwise
    """
    if type(obj) is a_class:
        return True
    else:
        return False
    