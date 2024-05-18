#!/usr/bin/python3
"""
Unit tests for the Review class.
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class ReviewTestCase(unittest.TestCase):
    """
    Test suite for the Review class.
    """

    def test_instance_creation(self):
        """
        Test if Review is a subclass of BaseModel.
        """
        review_instance = Review
        self.assertTrue(issubclass(review_instance, BaseModel))

