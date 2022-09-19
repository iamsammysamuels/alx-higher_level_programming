#!/usr/bin/python3

"""A module with a class Rectangle that defines a rectangle
"""


class Rectangle:
    """Defines a rectangle with height and width.
    """

    def __init__(self, width=0, height=0):
        """Initialises the rectangle with the arguments values.

        Attributes:
            width: (:obj: 'int', optional): height of the rectangle.
            height: (:obj 'int', optional): width of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Gets the argument.

        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Checks errors and sets for size attribute

        Attributes:
            value: (:obj: 'int') value to assign
            to the object after error checks.

            Raises:
                TypeError: Exception if width is not an integer.
                ValueError: Exception if width is less than zero.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        else:
            self.__width = value

    @property
    def height(self):
        """Gets the value of height

        Returns:
            The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of the object with value attribute

        Attribute:
            value: (:obj: 'int') value to
            assign to the object after error checks.

        Raises:
            TypeError: Exception if the value is not an int.
            ValueError: Exception if the value is less than zero.
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        else:
            self.__height = value
