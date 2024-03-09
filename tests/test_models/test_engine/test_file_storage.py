#!/usr/bin/python3
''' Unit tests for FileStorage module '''

import os
import json
import models
import unittest
from unittest.mock import mock_open, patch
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    ''' Unit tests for FileStorage module '''

    def test_init(self):
        ''' Test init method '''
        self.my_store = FileStorage()
        self.file_path = 'test_file.json'
        FileStorage.__file_path = self.file_path
        FileStorage.__objects = self.objects
        self.assertIsInstance(models.storage, FileStorage)

    def test_file_path(self):
        ''' Test file_path '''
        self.assertEqual(type(self.my_store.all()), dict)
        self.assertEqual(str, type(self.my_store.__file_path))

    def test_objects(self):
        ''' Test __objects '''
        self.assertEqual(dict, type(self.my_store.__objects))

    def test_all(self):
        ''' Test all method '''
        self.assertEqual(len(self.my_store.all()), 12)

    def test_new(self):
        ''' Test new method '''
        m = BaseModel()
        models.storage.new(m)
        self.assertIn('BaseModel.'+ m.id, models.storage.all().keys())
        self.assertIn(m, models.storage.all().values())

    # @patch('builtins.open', new_callable=mock_open)
    # @patch('json.dump')
    def test_save_1(self):
        ''' Test save method '''
        m = BaseModel()
        self.my_store.new(m)
        m.save()
        # mock_open.assert_called_once_with(self.file_path, 'w')
        # mock_json_dump.assert_called_once_with(self.objects, mock_open())
        new_store = FileStorage()
        new_store.reload()
        objects = new_store.all()
        self.assertEqual(len(objects), 13)
        obj_key = f'{type(m).__name__}.{m.id}'
        self.my_store.reload()
        self.assertIn(obj_key, objects)

    def test_save_2(self):
        """ Test save method """
        path = FileStorage.__file_path

        new_obj = {k: FileStorage.__objects[k].to_dict()
                   for k in FileStorage.__objects.keys()}

        with open(path, 'w') as f:
            json.dump(new_obj, f)

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
