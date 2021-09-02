from pydantic import BaseModel, Field
from pymongo import *
from bson import ObjectId
from typing import Optional

client = MongoClient("mongodb+srv://ilkinm:Spiderman11A@cluster0.aog30.mongodb.net/volue?retryWrites=true&w=majority")
db = client.volue

# Defining _id field for mongodb / special class for mongodb.
class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')

# Class model for customer data.
class CustomerData(BaseModel):
    _id: Optional[PyObjectId] = Field(alias='_id')
    name: str
    t: int
    v: float

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
