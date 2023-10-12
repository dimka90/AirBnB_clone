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

    def test_str_(self):
        """
        A function that test for the string representation of an instance
        """
        obj = BaseModel()
        self.assertEqual(obj.__str__, "[{}] ({}) {}".format(obj.__class__.__name__, obj.id, obj.__dict__))

    def test_save(self):
        """
        A function that saves the state of an object
        """
        obj = BaseModel()
        obj.save()
        self.assertTrue(hasattr(obj, "save"))

        self.assertTrue(obj.updated_at, datetime.now())

    def test_dict(self):
        """
        A function that returns the dictionary representation in a 
        dictionary format
        """

        obj = BaseModel()
        self.assertTrue(hasattr(obj,"to_dict"))

        dict_obj = obj.to_dict()

        self.assertTrue(dict_obj, {"id":obj.id, "__class__":self.__class__.__name__, "created_at":obj.created_at, "updated_at":obj.updated_at})

    def test_kwarg(self):
        """
        A function that test for the creation of an instance from
        a dictionary
        """
        obj = BaseModel()
        dict_obj = obj.to_dict()
        obj1 = BaseModel(**dict_obj)
        self.assertTrue(hasattr(obj1, "id"))
        self.assertIsInstance(obj1, BaseModel)
        self.assertTrue(hasattr(obj1, "__class__"))







