#!/usr/bin/python3
"""Review class module"""
import json
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    place_id = ""
    user_id = ""
    text = ""
