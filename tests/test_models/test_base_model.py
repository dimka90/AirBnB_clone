#!/usr/bin/python3
"""
A module that test the Basemodel class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    """

    def test_basemodel(self):
        """
        """
        obj = BaseModel()
        obj1 = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(hasattr(obj, "id"))
        self.assertIsInstance(obj.id, str)
        self.assertNotEqual(obj.id, obj1.id)
