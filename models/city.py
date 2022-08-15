#!/usr/bin/python3
"""city module."""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines attributes/models for City objects."""

    state_id = ""
    name = ""
