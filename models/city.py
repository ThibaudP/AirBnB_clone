#!/usr/bin/python3
"""City class module"""
import json
from models.base_model import BaseModel


class City(BaseModel):
    """City class"""

    def __init__(self, *args, **kwargs):
        """Constructor for City"""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
