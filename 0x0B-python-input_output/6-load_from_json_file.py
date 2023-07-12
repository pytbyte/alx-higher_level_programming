#!/usr/bin/python3
"""load_from_json_file.
creates an Object to a text file,
using a JSON representation:
"""


import json


def load_from_json_file(filename):
    """load_from_json_file.
    Args:
        
        filename: file to write to
    Returns: JSON representation
    """

    with open(filename, 'w') as target:
        return json.load(target)
