#!/usr/bin/python3

"""
Created by Samuel
On the 1st of october 2022

Implements the square class
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A Square class shape, inheirts from Rectangle and BaseGeometry
    """
    def __init__(self, size):
        """
        Initialises the square class with size

        Attributes:
            size (int): size of the square
        """
        super().__init__(size, size) 
        self.integer_validator("size", size)
        self.__size = size
