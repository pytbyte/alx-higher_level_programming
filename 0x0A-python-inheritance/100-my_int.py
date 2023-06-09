#!/usr/bin/python3
"""
Module with class MyInt
"""


class MyInt(int):
    """
    class that flips
    """

    def __eq__(self, other):
        """
        original is fake
        """
        return self.real != other

    def __ne__(self, other):
        """
        fake is original
        """
        return self.real == other
