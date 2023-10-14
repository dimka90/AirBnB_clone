#!/usr/bin/python3
""" A user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    a class that represent the instance of a User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        a function that inititalise the instance of a class
        """
        super().__init__(*args, **kwargs)
