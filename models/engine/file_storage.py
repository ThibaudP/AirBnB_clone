#!/usr/bin/python3
"""FileStorage class module"""
import json
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


class FileStorage():
    """FileStorage class.

    Serializes/deserializes instances to and from JSON"""

    __file_path = "classes.json"
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
        if self.__file_path is not None:
            with open(self.__file_path, "r") as file:
                try:
                    json_objects = json.load(file)
                    for key in json_objects:
                        class_name = classes[json_objects[key]["__class__"]]
                        self.__objects[key] = class_name(**json_objects[key])
                except:
                    pass
