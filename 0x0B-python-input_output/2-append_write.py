#!/usr/bin/python3
"""_append_file_ : function that creates,
                opens, appends and
                prints character count
"""


def append_file(filename="", text=""):
    """_append_file_ : handles the create
                    open, append and char
                    counter.
        Args:
        filename (str): the name of the
                        file you intend
                        to append to.
        text (str): the text to append
                    into the file.
    """

    with open(filename, 'a') as target:
        return target.write(text)
