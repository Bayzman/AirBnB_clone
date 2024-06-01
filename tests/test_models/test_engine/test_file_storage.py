#!/usr/bin/python3

""" Unittests for FileStorage """

import unittest
import json
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ Unittests for FileStorage module """
    def setUp(self):
        """ set up """
        self.storage = FileStorage()
        self.storage.__objects = {}

    def test_all(self):
        """ Test all method """
        self.assertEqual(self.storage.all(), None)

    def test_new(self):
        """ Test the new method """
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(f'BaseModel.{obj.id}', self.storage.__objects)

    def test_save(self):
        """ Test the save method """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open('file.json', 'r') as f:
            data = json.load(f)
            self.assertIn(f'BaseModel.{obj.id}', data)

    def test_reload(self):
        """ Test the reload method """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.__objects = {}
        self.storage.reload()
        self.assertIn(f'BaseModel.{obj.id}', self.storage.__objects)

    def test_reload_no_file(self):
        """ Test reload without any file """
        self.storage.reload()
        self.assertEqual(self.storage.__objects, {})


if __name__ == '__main__':
    unittest.main()
