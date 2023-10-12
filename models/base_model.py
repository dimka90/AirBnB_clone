#!/usr/bin/python3

"""
A python module that create a Baseclass model
that other classes will inherit from
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    This is a Baseclass that other class that creat a unique id and
    other attributes that will different each class from the other
    """

    def __init__(self, *args, **kwargs):
        """
        A function that initialise the state of an object
        """
        keys_to_include = ["id", "created_at", "updated_at"]

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class___':
                    continue
                elif key == 'updated_at':
                    value == datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif 'id' not in kwargs.keys():
                    self.id = str(uuid.uuid4())
                elif 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                elif 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        A function that gives the string representation of the instance
        """

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        A function that update the value of the updated object
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        A function that returns the dictionay representation of an 
        instance object
        """
        dict_obj = self.__dict__

        dict_obj["__class__name"] = self.__class__.__name__
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.updated_at.isoformat()


        return dict_obj
