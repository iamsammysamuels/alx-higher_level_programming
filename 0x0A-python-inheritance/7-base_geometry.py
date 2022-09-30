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

    def integer_validator(self, name, value):
        """validates value

        Attributes:
            name (str): name assigned to value
            value (int): the value to be validated

        Raises:
            ValueError: if value is not an integer
            TypeError: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
