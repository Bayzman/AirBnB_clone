#!/usr/bin/python3

""" File storage class """

import json
import os


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
        self.__object[key] = obj

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
                self.__objects = {}
                for key, obj_dict in json.load(f).items():
                    obj_class = globals()[obj_dict["__class__"]]
                    obj = obj_class(**obj_dict)
                    self.new(obj)