#!/usr/bin/python3
"""Review class module"""
import json
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""

    def __init__(self, *args, **kwargs):
        """Constructor for Review"""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
