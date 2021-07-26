from typing import List
from fastapi import APIRouter, Response
from ..lib.schemas import Product
from ..lib.database import get_products as get_db_products

router = APIRouter(
    prefix="/products",
    tags=["products"]
)


@router.get("", response_model=List[Product])
async def get_products(response: Response):
    response.headers["Cache-Control"] = "public, max-age=9000"
    return get_db_products()
