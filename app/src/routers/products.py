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
        {"id": 1, "title": "Kiri", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "price": Decimal('4.99')},
        {"id": 2, "title": "Bambus II", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "price": Decimal('2.49')}
    ]
