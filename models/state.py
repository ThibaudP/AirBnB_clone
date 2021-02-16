#!/usr/bin/python3
"""State class module"""
import json
from models.base_model import BaseModel


class State(BaseModel):
    """State class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor for State"""
        super().__init__(*args, **kwargs)
