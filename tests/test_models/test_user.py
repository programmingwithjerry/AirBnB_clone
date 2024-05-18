#!/usr/bin/python3
"""
Unit tests for the User class.
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Test suite for the User class.
    """

    def test_instance_creation(self):
        """
        Verify that a User instance can be created.
        """
        user_instance = User()
        self.assertTrue(isinstance(user_instance, User))

