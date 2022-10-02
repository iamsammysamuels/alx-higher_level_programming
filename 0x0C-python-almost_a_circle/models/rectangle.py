#!/usr/bin/python3

"""
Created by Samuel Ezeh
On the 2nd of oct. 2022
"""


from models.base import Base as Base


class Rectangle(Base):
    """
    A class Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        A class constructor to initialise the instance attributes

        Attributes:
            height (int, private): height of the Rectangle
            width (int, private): width of the Rectangle
            x (int, private): x
            y (int, private): y
            id (int, optional): id of the instance
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
    @property
    def height(self):
        """
        Gets the height of the Rectangle

        Returns: The height of the Rectangle
        """
        return self.__width

    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectangle

        Attribute:
            height (int, private): height

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 1
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 1:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        Gets the width of the Rectangle

        Returns: The width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Sets the width of the Rectangle

        Attribute:
            width (int, private): width
        
        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 1
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 1:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def x(self):
        """
        Gets x

        Returns: x
        """
        return self.x
    
    @x.setter
    def x (self, x):
        """
        Sets x

        Attribute:
            x (int, private): x

        Raises:
            TypeError: If x is not an integer
            ValueError: If x is less than 0
        """
        if type(x) != int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y (self):
        """
        Gets y

        Returns: y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Sets y

        Attribute:
            y (int, private): y
        
        Raises:
            TypeError: If x is not an integer
            ValueError: If y is less tha 0
        """
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
