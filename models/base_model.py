#!/usr/bin/python3

"""
A python module that create a Baseclass model
that other classes will inherit from
"""
import uuid


class BaseModel:
    """
    This is a Baseclass that other class that creat a unique id and
    other attributes that will different each class from the other
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
