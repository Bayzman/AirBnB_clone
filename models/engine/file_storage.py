#!/usr/bin/python3

""" File storage class """

import json
import os
import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """ The FileStorage class serializes instances to a JSON file
        and deserializes JSON files to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to a JSON file """
        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict()
                       for key, obj in self.__objects.items()}, f)

    def reload(self):
        """ Deserializes a JSON file __file_path to __objects, if it exists
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_json = json.load(f)
                for obj in obj_json.values():
                    obj_class = obj["__class__"]
                    # del obj['__class__']
                    self.new(eval(obj_class)(**obj))
