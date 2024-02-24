#!/usr/bin/python3
''' Unit tests for FileStorage module '''

import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    ''' Unit tests for FileStorage module '''

    def test_init(self):
        ''' Test init method '''
        self.my_store = FileStorage()
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_file_path(self):
        ''' Test file_path '''
        self.assertEqual(str, type(self.my_store.__file_path))

    def test_objects(self):
        ''' Test __objects '''
        self.assertEqual(dict, type(self.my_store.__objects))

    def test_all(self):
        ''' Test all method '''
        self.assertEqual(len(self.my_store.all()), 13)

    def test_new(self):
        ''' Test new method '''
        m = BaseModel()
        models.storage.new(m)
        self.assertIn('BaseModel.'+ m.id, models.storage.all().keys())
        self.assertIn(m, models.storage.all().values())

    def test_save(self):
        ''' Test save method '''
        m = BaseModel()
        models.storage.new(m)
        models.storage.save()
        save_text = ''
        with open('file.json', 'r') as f:
            save_text = f.read()
            self.assertIn('BaseModel.' + m.id, save_text)

    def test_reload(self):
        ''' Test reload method '''
        m = BaseModel()
        models.storage.new(m)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn('BaseModel.' + m.id, objs)


if __name__ == '__main__':
    unittest.main()
