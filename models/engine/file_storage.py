#!/usr/bin/python3

import json
from datetime import datetime


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def to_dict(self):
        """returns a dictionary containing all objects in __objects"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        return new_dict

    def save(self):
        """Serialize the file storage to a JSON file"""
        objects = self.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(objects, f)

    def reload(self):
        """deserialize the JSON file to objects"""
        from models.base_model import BaseModel
        from models.user import User
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                objects = json.load(f)
            for key, value in objects.items():
                self.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            pass
