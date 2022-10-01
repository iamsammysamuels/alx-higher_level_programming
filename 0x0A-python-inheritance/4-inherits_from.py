#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Created by Samuel Ezeh
On the 27th of sept 2022

Implements  a function that returns True if the object
is an instance of a class that inherited (directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """function that checks if the object is an instance of a class that inherited from the specified class

        Args:
            obj: could be any type
            a_class (type): type to check against

        Returns: a boolean
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
            return True
    return False
