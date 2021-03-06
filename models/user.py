#!/usr/bin/python3
"""User class module"""
import json
from models.base_model import BaseModel


class User(BaseModel):
    """User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Constructor for User"""
        super().__init__(*args, **kwargs)
