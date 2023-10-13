#!/usr/bin/python3
"""
Class  that serializes instances to a
JSON file and deserializes JSON file to instances
"""
import json
import os

class FileStorage:
    """ Class that serializes and deserializes JSON objects """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects


    def reload(self):
        """  deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State

        dctn = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity,
                'City': City, 'Place': Place, 'Review': Review, 'State': State}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(dctn[value['__class__']](**value))


    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        dictn = {}
        for k, v in FileStorage.__objects.items():
            dictn[k] = v.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dictn, f)


    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        k = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[k] = obj
