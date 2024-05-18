#!/usr/bin/python3
"""
Handles the conversion between JSON and instances.
"""
import json
import sys
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    Manages the serialization of instances to a JSON file and
    deserialization of JSON file to instances.

    Attributes:
    __file_path: The path to the JSON file.
    __objects: A dictionary storing all instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary storing all instances.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary with a key
        in the format <class name>.id.
        """
        key = obj.__class__.__name__ + "." + getattr(obj, "id")
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the objects in the storage dictionary to a JSON file.
        """
        with open(FileStorage.__file_path, mode='w', encoding='UTF-8') as f:
            obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            json_str = json.dumps(obj_dict)
            f.write(json_str)

    def reload(self):
        """
        Deserializes the JSON file to the storage dictionary.
        """
        try:
            with open(FileStorage.__file_path, mode='r') as f:
                obj_data = json.load(f)
                for key, value in obj_data.items():
                    class_name = key.split('.')[0]
                    obj = eval(class_name)(**value)
                    self.new(obj)
        except Exception:
            pass

