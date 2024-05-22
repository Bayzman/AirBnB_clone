#!/usr/bin/python3

""" Unit test for User class """
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime, date


class TestUser(unittest.TestCase):
    """ Unit tests for User class """
    def test_email(self):
        """ Test email attribute """
        user1 = User()
        user2 = User()
        user2.email = 'admin@alx.com'
        self.assertEqual(user1.email, '')
        self.assertEqual(user2.email, 'admin@alx.com')

    def test_password(self):
        """ Test password attribute """
        user1 = User()
        user2 = User()
        user2.password = 'password'
        self.assertEqual(user1.password, '')
        self.assertEqual(user2.password, 'password')

    def test_firstname(self):
        """ Test first name attribute """
        user1 = User()
        user2 = User()
        user2.first_name = 'Tiger'
        self.assertEqual(user1.first_name, '')
        self.assertEqual(user2.first_name, 'Tiger')

    def test_lastname(self):
        """ Test last name attribute """
        user1 = User()
        user2 = User()
        user2.last_name = 'Woods'
        self.assertEqual(user1.last_name, '')
        self.assertEqual(user2.last_name, 'Woods')


if __name__ == '__main__':
    unittest.main()
