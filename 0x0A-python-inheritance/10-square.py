#!/usr/bin/python3

"""
Created by Samuel Ezeh
On the 30th of sept 2022

Implements the square class that inherits from the rectangle
"""


rectangle = __import__("9-rectangle").Rectangle

class Square(rectangle):
    """
    A Square class shape, inheirts from
    Rectangle and BaseGeometry
    """
    def __init__(self, size):
        """
        initialises square class

        Attributes:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        Implements the str function

        Returns:
            The str format of the instance
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        Implements the area of the square

        Returns:
            The area of the square
        """
        return self.__size * self.__size
