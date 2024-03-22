#!/usr/bin/python3

""" Unit test for Amenity """

from models.base_model import BaseModel
from models.amenity import Amenity
import unittest
from datetime import datetime, date


class TestAmenity(unittest.TestCase):
    """ Unit test for Amenity """

    def test_amenity_instance(self):
        """ Amenity instance """
        amen = Amenity()
        self.assertIsInstance(amen, BaseModel)

    def test_amenity_name(self):
        """ Amenity name """
        amen1 = Amenity()
        amen2 = Amenity()
        amen2.name = 'Gym'
        self.assertEqual(amen1.name, '')
        self.assertEqual(amen2.name, 'Gym')


if __name__ == '__main__':
    unittest.main()
