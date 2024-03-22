#!/usr/bin/python3

""" Unit test for State """

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ Unit test for State """

    def test_state_instance(self):
        """ State instance """
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_state_name(self):
        """ State name """
        state1 = State()
        state2 = State()
        state2.name = 'Abia'
        self.assertEqual(state1.name, '')
        self.assertEqual(state2.name, 'Abia')


if __name__ == "__main__":
    unittest.main()
