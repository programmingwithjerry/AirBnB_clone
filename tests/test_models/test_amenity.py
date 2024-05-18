#!/usr/bin/python3
"""
Unit tests for the Amenity class.
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test suite for the Amenity class.
    """

    def test_instance_creation(self):
        """
        Test that an instance of Amenity can be created.
        """
        amenity_instance = Amenity()
        self.assertTrue(isinstance(amenity_instance, Amenity))

