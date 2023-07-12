#!/usr/bin/python3
"""from_json_string.
Returns the JSON representation of an object.
"""


import json


def from_json_string(my_str):
    """from_json_string.
    Args:
        - my_obj: string to represent
    Returns: JSON representation
    """

    return json.loads(my_str)
