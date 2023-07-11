#!/usr/bin/python3
"""
adds a new attribute to an object if it’s possible
"""


def add_attribute(a_class, proerty_name, property_value):
    """
    adds a new attribute to an object if it’s possible
    checks if they object can take type given.
    """
    if not hasattr(a_class, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(a_class, proerty_name, property_value)
