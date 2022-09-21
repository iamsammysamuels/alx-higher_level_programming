#!/usr/bin/python3
"""A module with a class LockedClass with no
class or object attribute, that prevents
the user from dynamically creating new
instance attributes, except if the new
instance attribute is called first_name.
"""


class LockedClass:
    """A locked class that only lets the user dynamically create
    the instanceattribute 'first_name'"""
    __slots__ = ['first_name']
