#!/usr/bin/python3
"""
Unit tests for the Place class.
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Test suite for the Place class.
    """

    def test_instance_creation(self):
        """
        Verify that a Place instance can be created.
        """
        place_instance = Place()
        self.assertTrue(isinstance(place_instance, Place))

