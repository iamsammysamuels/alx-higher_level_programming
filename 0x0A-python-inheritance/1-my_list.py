#!/usr/bin/python3

"""Module created by Samuel Ezeh
On the 27th of sept 2022
"""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        """A function that prints a sorted list"""
        list_cpy = self[:]
        list_cpy.sort()
        print("{}".format(list_cpy))
