from typing import List
from fastapi import APIRouter
from ..lib.schemas import Product
from ..lib.database import get_products as get_db_products

router = APIRouter(
    prefix="/products",
    tags=["products"]
)


@router.get("", response_model=List[Product])
async def get_products():
    return get_db_products()
