#!/usr/bin/python3
"""
Unit tests for the Review class.
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Test suite for the Review class.
    """

    def test_instance_creation(self):
        """
        Verify that Review is a subclass of BaseModel.
        """
        review_class = Review
        self.assertTrue(issubclass(review_class, BaseModel))

