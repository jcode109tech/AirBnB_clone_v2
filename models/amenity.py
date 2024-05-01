#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

class Amenity(BaseModel, Base):
    """ Amenity """
    if models.storage_type == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                    viewonly=False)
    else:
        name = ""
