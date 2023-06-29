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

    @staticmethod
    def from_json_string(json_string):
        """Converts JSON string to list of dictionaries"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
    
        if type(list_objs[0]).__name__ == "Rectangle":
            new_dict = [item.to_dictionary() for item in list_objs]
            json_string = cls.to_json_string(new_dict)
            json.dump(new_dict, json_file)

        json_file.close()
