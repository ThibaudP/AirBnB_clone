#!/usr/bin/python3
"""FileStorage class module"""
import json
from os import path
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage():
    """FileStorage class.

    Serializes/deserializes instances to and from JSON"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dict containing all objects"""
        return self.__objects

    def new(self, obj):
        """sets in `__object` the `obj` with key `obj_class_name.id`"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __object to the JSON file"""
        if self.__file_path is not None:
            json_objects = {}
            for key in self.__objects:
                json_objects[key] = self.__objects[key].to_dict()
            with open(self.__file_path, 'w') as file:
                json.dump(json_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as file:
                json_objects = json.load(file)
                for key in json_objects:
                    class_name = classes[json_objects[key]["__class__"]]
                    # obj = class_name(**json_objects[key])
                    # self.new(obj)
                    self.__objects[key] = class_name(**json_objects[key])
        except:
            pass
