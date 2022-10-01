#!/usr/bin/python3

"""
Created by Samuel Ezeh
On the 30th of sept 2022

Initialises the rectangle class that inherits from
the BaseGeometry class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from the BaseGeometry"""
    def __init__(self, width, height):
        """
        initialises the Rectangle class

        Attributes:
            width (int): width of the Rectangle
            height (int): the height of the rectangle
        """
        self.integer_validator(str(width), width)
        self.integer_validator(str(height), height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        returns the rectangle description

        Returns:
            Rectangle description
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Implements the area of the rectangle

        Returns:
            The are of the rectangle
        """
        return self.__width * self.__height
