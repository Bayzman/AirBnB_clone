#!/usr/bin/python3

""" Unittest for BaseModel """

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Test BaseModel """
    def setUp(self):
        """ Setup instance """
        self.bm = BaseModel()

    def test_init(self):
        """ Test constructor """
        self.assertIsInstance(self.bm, BaseModel)
        self.assertIsInstance(self.bm.id, str)
        self.assertIsInstance(self.bm.created_at, datetime)
        self.assertIsInstance(self.bm.updated_at, datetime)

    def test_str(self):
        """ Test __str__ """
        self.assertIsInstance(self.bm.__str__(), str)
        self.assertIn(self.bm.id, self.bm.__str__())
        self.assertIn(self.bm.__class__.__name__, self.bm.__str__())

    def test_save(self):
        """ Test save """
        created_at = self.bm.created_at
        updated_at = self.bm.updated_at
        self.bm.save()
        self.assertNotEqual(self.bm.updated_at, updated_at)
        self.assertEqual(self.bm.created_at, created_at)

    def test_to_dict(self):
        """ Test to_dict """
        dict_repr = self.bm.to_dict()
        self.assertIsInstance(dict_repr, dict)
        self.assertIn('id', dict_repr)
        self.assertIn('created_at', dict_repr)
        self.assertIn('updated_at', dict_repr)
        self.assertIn('__class__', dict_repr)
        self.assertEqual(dict_repr['__class__'], self.bm.__class__.__name__)
        self.assertEqual(dict_repr['id'], self.bm.id)
        self.assertEqual(datetime.fromisoformat(dict_repr['created_at']),
                         self.bm.created_at)
        self.assertEqual(datetime.fromisoformat(dict_repr['updated_at']),
                         self.bm.updated_at)


if __name__ == '__main__':
    unittest.main()
