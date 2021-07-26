from decimal import Decimal
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    title: str
    description: str
    price: Decimal


class User(BaseModel):
    id: int
    username: str
