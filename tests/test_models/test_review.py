#!/usr/bin/python3

""" Unit test for Review """

from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """ Unit test for Review """

    def test_review_instance(self):
        """ Review instance """
        rev = Review()
        self.assertIsInstance(rev, BaseModel)

    def test_review_place_id(self):
        """ Review place_id """
        rev1 = Review()
        rev2 = Review()
        rev2.place_id = 'AL'
        self.assertEqual(rev1.place_id, '')
        self.assertEqual(rev2.place_id, 'AL')

    def test_review_user_id(self):
        """ Review user_id """
        rev1 = Review()
        rev2 = Review()
        rev2.user_id = 'James'
        self.assertEqual(rev1.user_id, '')
        self.assertEqual(rev2.user_id, 'James')

    def test_review_text(self):
        """ Review text """
        rev1 = Review()
        rev2 = Review()
        rev2.text = 'Some review text'
        self.assertEqual(rev1.text, '')
        self.assertEqual(rev2.text, 'Some review text')


if __name__ == '__main__':
    unittest.main()
