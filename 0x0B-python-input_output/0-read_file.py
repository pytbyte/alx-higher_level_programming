#!/usr/bin/python3
"""_read_file_ : function that
                opens, reads and
                prints to stdout
"""


def read_file(filename=""):
    """_read_file_ : handles the
                    read, write and
                    close ops
    Args:
        filename (str): the name of the
                        file you intend
                        to read.
    """
    with open(filename) as target:
        content = target.read()
        print(content, end="")
