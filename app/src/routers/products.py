from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from decimal import Decimal

router = APIRouter(
    prefix="/products",
    tags=["products"]
)


class Product(BaseModel):
    title: str
    description: str
    price: Decimal


@router.get("", tags=["products"], response_model=List[Product])
async def get_products():
    return [
        {"title": "orchids", "description": "colorful", "price": Decimal('4.99')},
        {"title": "ficus", "description": "delicious", "price": Decimal('2.49')}
    ]
