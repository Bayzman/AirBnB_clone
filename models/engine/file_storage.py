#!/usr/bin/python3
''' File storage class '''

import json
from models.base_model import BaseModel


class FileStorage:
    ''' The FileStorage class serializes instances to a JSON file
        and deserializes JSON file to instances
    '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' Returns the dictionary __objects '''

        return FileStorage.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''

        key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        ''' Serializes __objects to a JSON file '''
        obj = {k: FileStorage.__objects[k].to_dict()
               for k in FileStorage.__objects.keys()}

        with open(self.__file_path, 'w') as f:
            json.dump(obj, f)

    def reload(self):
        ''' Deserialize a JSON file __file_path to __objects,
            if it exists
        '''
        try:
            with open(FileStorage.__file_path) as f:
                obj_json = json.load(f)
                for obj in obj_json.values():
                    cls_name = obj['__class__']
                    del obj['__class__']
                    self.new(eval(cls_name)(**obj))

        except FileNotFoundError:
            return
