#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from os import getenv
from sqlalchemy import Column, String, DateTime, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
import models

time = "%Y-%m-%dT%H:%M:%S.%f"

if models.storage_type == "db":
    Base = declarative_base()
else:
    Base = object

class BaseModel:
    """A base class for all hbnb models"""
    if models.storage_type == "db":
        id = Column(VARCHAR(60), primary_key=True, nullable=False, unique=True)
        created_at = Column(DateTime, default=datetime.now(), nullable=False) 
        updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # storage.new(self)
        else:
            for key, value in kwargs.items():
               if key != "__class__":
                   setattr(self, key, value)
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
               self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.updated_at_at = datetime.now()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
               self.updated_at_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at_at = datetime.now()
                          

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        if dictionary['_sa_instance_state']:
            del dictionary['_sa_instance_state']
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
    
    def delete(self):
        """Deletes a  model instance from the storage"""
        from models import storage
        storage.delete(self)
