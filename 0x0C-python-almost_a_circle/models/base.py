#!/usr/bin/python3

"""
Created by Samuel Ezeh
On the 2nd of oct. 2022
"""


class Base:
    """
    A class, base

    Attributes:
        nb_objects (int, private): number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        The constructir method

        Attributes:
            id (int): id of the objects
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
