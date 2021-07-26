from typing import List, Optional
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


class ShippingAddress(BaseModel):
    fullname: str
    address_line1: str
    address_line2: Optional[str]
    zip: str
    city: str
    country: str


class OrderItem(Product):
    quantity: int
    total: Decimal


class Order(BaseModel):
    id: int
    label: str
    user_id: int
    shipping_address: ShippingAddress
    items: List[OrderItem]
    total: Decimal


class OrderItemRequest(BaseModel):
    id: int
    quantity: int


class OrderRequest(BaseModel):
    shipping_address: ShippingAddress
    items: List[OrderItemRequest]
