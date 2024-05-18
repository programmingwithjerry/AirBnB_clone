#!/usr/bin/python3
"""
Unit tests for the Place class.
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class PlaceTestCase(unittest.TestCase):
    """
    Test suite for the Place class.
    """

    def test_instance_creation(self):
        """
        Test creating an instance of Place.
        """
        place_instance = Place()
        self.assertTrue(isinstance(place_instance, Place))

