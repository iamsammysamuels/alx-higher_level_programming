#!/usr/bin/python3

"""A module created by Samuel Ezeh
On the 27th of sept 2022
"""



def is_kind_of_class(obj, a_class):
    """A function to check if an object is an instance of a specified class

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Return:
        true if the objecect is an instance else, false
    """
    return (isinstance((obj), a_class))
