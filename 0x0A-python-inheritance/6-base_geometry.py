#!/usr/bin/python3

"""
Created by Samuel Ezeh
On the 30th of sept 2022

Creates an empty class with a function that raises an Exception
"""


class BaseGeometry:
    """
    Uninitialised yet
    """
    def area(self):
        """
         Public instance method that calculates the area

         Raises:
            Exception if area is not imlemented
        """
        raise Exception("area() is not implemented")
