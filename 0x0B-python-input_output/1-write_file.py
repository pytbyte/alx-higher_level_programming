#/usr/bin/python3
"""_Write_file_ : function that creates,
                opens, writes and 
                prints character count
"""


def write_file(filename="", text=""):
    """_write_file_ : handles the create
                    open, write and char
                    counter.
                    
    Args:
        filename (str): the name of the 
                        file you intend
                        to write to.
        text (str): the text to write
                    into the file.
    """

    with open(filename, 'w+') as target:
        return target.write(text)
