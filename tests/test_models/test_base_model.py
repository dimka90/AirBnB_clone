#!/usr/bin/python3
"""
A module that test the Basemodel class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    """

    def test_basemodel(self):
        """
        A function that test the instances of base model
        Args:
            self(object): An instance of the TestBaseModel
        Return:
              Result of test
        """
        obj = BaseModel()
        obj1 = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj1, BaseModel)
        self.assertNotIsInstance(obj, int)
        self.assertNotEqual(obj, obj1)

    def test_uuid(self):
        """
        A function that test for the uniqueness of the id, and it datatype
        Args:
            self(object): An instance of the TestBaseModel
        Return:
              Result of test
        """
        obj = BaseModel()
        obj1 = BaseModel()
        self.assertTrue(hasattr(obj, "id"))
        self.assertIsInstance(obj.id, str)
        self.assertNotEqual(obj.id, obj1.id)
        self.assertIsNotNone(obj.id)

    def test_basetime(self):
        """
        A function that test for the time in which an object was created a
        time which an object was  updated
        Args:
            self(obj): Instance of the test class
        """
        obj = BaseModel()
        obj1 = BaseModel()
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertIsInstance(obj.created_at, datetime)
        self.assertNotEqual(obj.created_at, obj1.created_at)
        self.assertIsNotNone(obj.created_at)
        # testing the updated_at
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertEqual(obj.created_at, obj.updated_at)
        self.assertIsNotNone(obj.updated_at)
