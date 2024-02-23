#!/usr/bin/python3
''' Unit tests for BaseModel module '''

import os
from datetime import datetime, date
import unittest
from models.base_model import BaseModel
from time import sleep
import os


class TestBaseModel(unittest.TestCase):
    ''' Unit tests for BaseModel module '''

    def test_init(self):
        ''' Test init method '''
        m1 = BaseModel()
        self.assertIsNotNone(m1.id)
        self.assertIsInstance(m1.created_at, datetime)

    def test_str(self):
        ''' Test __str__ method '''
        m1 = BaseModel()
        self.assertIn(m1.__class__.__name__, str(m1))

    def test_instance_nequal(self):
        ''' Test instances of BaseModel '''
        m1 = BaseModel()
        m2 = BaseModel()
        self.assertNotEqual(m1, m2)

    def test_unique_ids(self):
        ''' Test for unique ids '''
        m1 = BaseModel()
        m2 = BaseModel()
        self.assertNotEqual(m1.id, m2.id)

    def test_created_at(self):
        ''' Test created_at attribute '''
        m1 = BaseModel()
        self.assertNotEqual(datetime.now(), m1.created_at)

    def test_updated_at(self):
        ''' Test updated_at attribute '''
        m1 = BaseModel()
        self.assertNotEqual(datetime.now(), m1.updated_at)

    def test_to_dict(self):
        ''' Test to_dict method '''
        m1 = BaseModel()
        m1_dict = m1.to_dict()
        self.assertIn('id', m1_dict)
        self.assertIn('created_at', m1_dict)
        self.assertIn('updated_at', m1_dict)

    def test_save(self):
        ''' Test save method '''
        m1 = BaseModel()
        sleep(0.20)
        m1_updated = m1.updated_at
        m1.save()
        self.assertLess(m1_updated, m1.updated_at)


if __name__ == '__main__':
    unittest.main()
