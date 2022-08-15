#!/usr/bin/python3
"""review module."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines attributes/models for Review objects."""

    place_id = ""
    user_id = ""
    text = ""
