#!/usr/bin/python3

""" Base Model Class """

import uuid
from datetime import datetime
import models


class BaseModel:
    """ BaseModel class that defines all common attributes and methods
        for other classes
    """

    def __init__(self, *args, **kwargs):
        """ Class constructor """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new()
        else:
            self.__dict__.update(kwargs)

    def __str__(self):
        """ Overwrites the print statement """
        class_name = self.__class__.__name__
        return f'[{class_name}] ({self.id}) {self.__dict__}'

    def save(self):
        """ Updates the public instance attribute updated_at with the
            current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__
            of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()

        return dict_copy
