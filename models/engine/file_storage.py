#!/usr/bin/python3

import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = str
    __objects = dict

    def __init__(self, file_path: str):
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self) -> None:
        """Serialize the file storage to a JSON file"""
        with open(self.__file_path, "w", encoding="utf-8") as file:
            objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
            file.write(json.dumps(objects))

    def reload(self) -> None:
        """deserialize the JSON file to objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                objects = json.loads(file.read())
                for key, value in objects.items():
                    class_name, obj_id = key.split(".")
                    if class_name == "User":
                        self.__objects[key] = User(**value)
                    elif class_name == "State":
                        self.__objects[key] = State(**value)
                    elif class_name == "City":
                        self.__objects[key] = City(**value)
                    elif class_name == "Amenity":
                        self.__objects[key] = Amenity(**value)
                    elif class_name == "Place":
                        self.__objects[key] = Place(**value)
                    elif class_name == "Review":
                        self.__objects[key] = Review(**value)
        except FileNotFoundError:
            pass
