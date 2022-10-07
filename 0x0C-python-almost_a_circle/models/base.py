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
            with open(filename, "w", encoding='utf-8') as file:
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
    
    @classmethod
    def create(cls, **dictionary):
        """"
        Implements an instance with all attributes already set

        Arguments:
            dictionary (dict): A double pointer to a dictionary

        Returns:
            An already set instance
            """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
         Implements a list of instances

         Returns:
            A list of instances or an empty list if the file doesn’t exist
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "r", encoding='utf-8') as file:
            read_file = file.read()
        dicts = cls.from_json_string(read_file)
        lists = []
        for values in dicts:
            inst = cls.create(**values)
            lists.append(inst)
        return lists
