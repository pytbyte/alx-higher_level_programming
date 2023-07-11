#!/usr/bin/python3
"""
100-my_int.
Creates a class that inherits from int.
"""


class MyInt(int):
    """
    inheriting from int,
    has == and != operators inverted
    """

    def __eq__(self, other):
        """
        Equal changes to unequal.
        """

        return super().__ne__(other)

    def __eq__(self, other):
        """
        unequality changes to equal.
        """

        return super().__ne__(other)

