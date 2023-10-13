#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
"""
A module that handles the serialization  and deserialization
of and python object, it saves the content to a json file 
"""

class FileStorage:
    """
    A class that handles file implementaition and 
    storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """A function that returns all the object stored in the 
        dictionary
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to the storage dictionary.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
         Serialize objects to JSON and save to file.
        """
        dictionary = {}
        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()
        # writing to the file using context manager
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(dictionary, file)

    def reload(self):
        """
        Deserialize JSON file to objects.
        """
        if os.path.isfile(FileStorage.__file_path):
        # Reading from json 
            with open(FileStorage.__file_path, "r", encoding = "utf-8") as file:
                data = json.load(file)
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                obj = eval(class_name)(**value)
                FileStorage.__objects[key] = obj
                #FileStorage.__objects[key] = eval(value['__class__'] (**value)) 

