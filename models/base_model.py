#!/usr/bin/python3
"""BaseModel class module"""
import uuid
import models
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """BaseModel class, from which all further classes will inherit from"""

    def __init__(self, *args, **kwargs):
        """Constructor for BaseModel"""
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
            if self.created_at and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if self.updated_at and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Informal string representation of BaseModel"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """Updates the `updated_at` attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a copy of the instance's `__dict__`"""
        inst_dict = self.__dict__.copy()
        if "created_at" in inst_dict:
            inst_dict["created_at"] = inst_dict["created_at"].isoformat()
        if "updated_at" in inst_dict:
            inst_dict["updated_at"] = inst_dict["updated_at"].isoformat()
        inst_dict["__class__"] = self.__class__.__name__

        return inst_dict
