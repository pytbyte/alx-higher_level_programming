#!/usr/bin/python3
""" class MyList
inherits from list
"""


class MyList(list):
    """Class MyList inherits from list."""

    def print_sorted(self):
        """Prints the list, in ascending sort."""

        list_with_inherited_data = self[:]
        list_with_inherited_data.sort()
        print("{}".format(list_with_inherited_data))
