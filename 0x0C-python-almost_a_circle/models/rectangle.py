#!/usr/bin/python3

"""
Created by Samuel Ezeh
On the 2nd of oct. 2022
"""
from models.base import Base


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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def height(self):
        """
        Gets the height of the Rectangle

        Returns: The height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Sets the height of the Rectangle

        Attribute:
            height (int, private): height

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 1
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def x(self):
        """
        Gets x

        Returns: x
        """
        return self.__x
    
    @x.setter
    def x(self, x):
        """
        Sets x

        Attribute:
            x (int, private): x

        Raises:
            TypeError: If x is not an integer
            ValueError: If x is less than 0
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
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
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
    
    def area(self):
        """
        Implememts the area value of the Rectangle instance

        Returns:
            The area of the Rectangle instance
        """
        return self.__height * self.__width

    def display(self):
        """
        that prints in stdout the Rectangle instance with the character #
        """
        for m in range(self.__y):
            print()
        for row in range(self.__height):
            for n in range(self.__x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Implements the string representation of the object

        Returns:
            The string representation of the object
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
    
    def update(self, *args, **kwargs):
        """
        Update the class Rectangle and assigns an argument to each attribute

        Attributes:
            args (int): Variable argument number.
        """
        if args is not None and len(args) != 0:
            for elm, arg in enumerate(args):
                if elm == 0:
                    self.id = arg
                elif elm == 1:
                    self.width = arg
                elif elm == 2:
                    self.height = arg
                elif elm == 3:
                    self.x = arg
                elif elm == 4:
                    self.y = arg
        
        elif kwargs is not None and len(kwargs) != 0:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Implements the dictionary representation of class Square

        Returns:
            The dictionary representation class square
        """
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height, 'width': self.width}
