#!/usr/bin/python3
"""
  class_to_json
    returns the dictionary description
    with simple data structure
    or JSON serialization of an object.
"""


def class_to_json(obj):
    """
    class_to_json
    returns the dictionary description
    with simple data structure
    or JSON serialization of an object.
    """
    return obj.__dict__
