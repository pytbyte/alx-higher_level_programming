#!/usr/bin/python3
"""
100-append_after.
Inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends the new_string after
    locating specific string.
    Args:
        filename: name of the file
        search_string: string to append after
        new_string: new_string to append
    """

    with open(filename, "r") as target_file:
        text = target_file.readlines()

    with open(filename, "w") as file_x:
        buffer = ""
        for content in text:
            buffer += content
            if search_string in content:
                buffer += new_string
        file_x.write(buffer)
