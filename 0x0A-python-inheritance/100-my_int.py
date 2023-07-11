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

    def __equal__(self, other):
        """
        Equal changes to unequal.
        """

        return super().__unequal__(other)

    def __unequal__(self, other):
        """
        unequality changes to equal.
        """

        return super().__equal__(other)
