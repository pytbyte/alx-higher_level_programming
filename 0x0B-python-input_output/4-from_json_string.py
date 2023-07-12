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

    return json.dumps(my_str)
#!/usr/bin/python3
"""Module 4-from_json_string.
Returns an object (Python data structure)
represented by a JSON string.
"""
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

    return json.dumps(my_str)


import json


def from_json_string(my_str):
    """Return the object represented my my_str.
    Args:
        - my_str: JSON string representation
    Returns: corresponding object
    """

    return json.loads(my_str)