#!/usr/bin/python3

"""
Created by Samuel Ezeh
On the 2nd of oct. 2022
"""
import json


class Base:
    """
    A class, base

    Attributes:
        nb_objects (int, private): number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        The constructir method

        Attributes:
            id (int): id of the objects
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Implements the JSON string representation of list_dictionaries

        Returns:
            The JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file

        Arguments:
            list_objs (instances): A list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        string = []
        if list_objs is not None and len(list_objs) != 0:
            for elem in list_objs:
                string_dict = cls.to_dictionary(elem)
                string.append(string_dict)
            json_dict = cls.to_json_string(string)
            with open(filename, "w", encoding='UTF-8') as file:
                file.write(json_dict)

    @staticmethod
    def from_json_string(json_string):
        """
        Implements the list of the JSON string representation

        Arguments:
            json_string (str): A string representing a list of dictionaries

        Returns:
            The list represented by json_string or an empty list
            if json_string is None or empty
        """
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)
