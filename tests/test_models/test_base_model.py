#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""
import models
from models.base_model import BaseModel
import datetime
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Test suite for the BaseModel class.
    """

    def test_base_model_instance(self):
        """
        Test various attributes and methods of BaseModel instances.
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertTrue(isinstance(instance1, BaseModel))
        self.assertNotEqual(instance1.id, instance2.id)
        instance1.name = "Holberton"
        self.assertEqual(instance1.name, "Holberton")
        self.assertTrue(isinstance(instance1.name, str))
        instance1.age = 5
        self.assertEqual(instance1.age, 5)
        self.assertTrue(isinstance(instance1.age, int))
        self.assertTrue(isinstance(instance1.created_at, datetime.datetime))
        self.assertTrue(isinstance(instance1.updated_at, datetime.datetime))
        self.assertTrue(isinstance(instance1.id, str))
        self.assertTrue(isinstance(instance1.to_dict(), dict))
        self.assertTrue(hasattr(instance1, 'id'))
        self.assertTrue(hasattr(instance1, 'created_at'))
        self.assertTrue(hasattr(instance1, 'updated_at'))
        self.assertTrue(hasattr(instance1, 'age'))
        self.assertTrue(hasattr(instance1, 'name'))
        self.assertTrue(hasattr(eval(instance1.__class__.__name__), '__str__'))
        
        instance_dict = instance1.to_dict()
        self.assertTrue(hasattr(instance_dict, '__class__'))

        self.assertTrue(hasattr(instance1, 'to_dict'))
        self.assertTrue(hasattr(instance1, '__str__'))

        self.assertTrue(callable(type(instance1.to_dict())))
        self.assertTrue(callable(type(instance1.__str__())))

        str_repr = str(instance1)
        self.assertMultiLineEqual(instance1.__str__(), str(instance1))

        expected_dict = {}
        for key, value in instance1.__dict__.items():
            if key in ['created_at', 'updated_at']:
                expected_dict[key] = value.isoformat()
            else:
                expected_dict[key] = value
        expected_dict['__class__'] = instance1.__class__.__name__

        self.assertDictEqual(instance1.to_dict(), expected_dict)

        initial_updated_at = instance1.updated_at
        instance1.save()
        stored_objects = models.storage.all()
        obj_key = 'BaseModel' + '.' + instance1.id
        if obj_key in stored_objects:
            stored_dict = stored_objects[obj_key].to_dict()
            for key, value in stored_dict.items():
                self.assertEqual(stored_dict[key], instance1.to_dict()[key])
        updated_updated_at = instance1.updated_at
        self.assertNotEqual(initial_updated_at, updated_updated_at)

        model_instance = BaseModel()
        model_instance.name = "Holberton"
        model_instance.number = 89
        model_instance_dict = model_instance.to_dict()
        for key in model_instance_dict.keys():
            self.assertTrue(
                hasattr(model_instance, key)
            )

