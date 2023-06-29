#!/usr/bin/python3
"""The base of the project"""
import json


class Base:
    """Private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to a file"""
        filename = type(list_objs[0]).__name__ + ".json"
        json_file = open(filename, "w")
        if list_objs is None:
            json.dump([], json_file)

    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to file"""
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, 'w') as file:
            file.write(json_string)
