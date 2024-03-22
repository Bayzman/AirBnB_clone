#!/usr/bin/python3

""" Unit test for Place """

from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """ Unit test for Place """

    def test_place_instance(self):
        """ Place instance """
        pl = Place()
        self.assertIsInstance(pl, BaseModel)

    def test_place_city_id(self):
        """ Place city_id """
        pl1 = Place()
        pl2 = Place()
        pl2.city_id = 'Tx'
        self.assertEqual(pl1.city_id, '')
        self.assertEqual(pl2.city_id, 'Tx')

    def test_place_user_id(self):
        """ Place user_id """
        pl1 = Place()
        pl2 = Place()
        pl2.user_id = 'Jay'
        self.assertEqual(pl1.user_id, '')
        self.assertEqual(pl2.user_id, 'Jay')

    def test_place_name(self):
        """ Place name """
        pl1 = Place()
        pl2 = Place()
        pl2.name = 'Texas'
        self.assertEqual(pl1.name, '')
        self.assertEqual(pl2.name, 'Texas')


if __name__ == '__main__':
    unittest.main()
