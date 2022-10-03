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

    def update(self, *args, **kwargs):
        """
        Update the class Rectangle and assigns an argument to each attribute

        Attributes:
            args (int): Variable argument number
            kwargs (int): Variable argument number with keywords
        """
        if args is not None and len(args) != 0:
            for elm, arg in enumerate(args):
                if elm == 0:
                    self.id = arg
                elif elm == 1:
                    self.size = arg
                elif elm == 2:
                    self.x = arg
                elif elm == 3:
                    self.y = arg
        elif kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
    def to_dictionary(self):
        """
        Implements the dictionary representation of a Square

        Returns:
            the dictionary representation class square
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
