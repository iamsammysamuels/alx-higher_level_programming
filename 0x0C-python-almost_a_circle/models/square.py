#!/usr/bin/python3

"""
Created by Samuel Ezeh
On the 3rd of oct. 2022
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        Implements the string representation of the object

        Returns:
            The string representation of the object
        """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__, self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """
        Gets the size of the square

        Returns:
            The size of the square
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Sets the size of the square
        
        Attribute:
            size (int, private): size
        """
        self.width = self.height = size
