#!/usr/bin/python3
"""save_to_json_file.
writes an Object to a text file,
using a JSON representation:
"""


import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file.
    Args:
        my_obj: string to represent
        filename: file to write to
    Returns: JSON representation
    """

    with open(filename, 'w') as target:
        json.dump(my_obj, target)
