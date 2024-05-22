#!/usr/bin/python3

""" Unit test for City """

from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """ Unit test for City """

    def test_city_instance(self):
        """ City instance """
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_state_id(self):
        """ City state id """
        city1 = City()
        city2 = City()
        city2.state_id = 'AL'
        self.assertEqual(city1.state_id, '')
        self.assertEqual(city2.state_id, 'AL')

    def test_city_name(self):
        """ City name """
        city1 = City()
        city2 = City()
        city2.name = 'Moscow'
        self.assertEqual(city1.name, '')
        self.assertEqual(city2.name, 'Moscow')


if __name__ == '__main__':
    unittest.main()
