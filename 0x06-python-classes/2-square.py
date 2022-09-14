#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines a Square class
"""

class Square:
    """
    A class Square that defines a square.

    Attribues:
        size: The size of the square.
    """
    def __init__(self, size=0):
        """
        The __init__ method for Square class

        Args:
            size: (:obj: 'int', optional): A private instance size
        Error Raises:
            TypeError: Exception if size is not an integer.
            ValueError: Exception if size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
