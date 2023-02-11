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
    __file_path = "file.json"
    __objects = {}

    def __init__(self, file_path: str):
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self) -> None:
        """Serialize the file storage to a JSON file"""
        objects_dict = {}
        for key, value in FileStorage.__objects.items():
            objects_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(objects_dict, file)

    def reload(self) -> None:
        """deserialize the JSON file to objects"""
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                FileStorage.__objects = {}
                objects = json.loads(file.read())
                for key, value in objects.items():
                    class_name, obj_id = key.split(".")
                    obj = eval(class_name)(**value)
                    """
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
                    """
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
