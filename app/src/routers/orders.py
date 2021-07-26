from fastapi import Depends, APIRouter, Body
from ..lib.schemas import User, OrderRequest
from ..lib.dependencies import get_current_user
from ..lib.database import add_order

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)


@router.post("")
async def create_order(order_request: OrderRequest = Body(..., embed=True), current_user: User = Depends(get_current_user)):
    order = add_order(order_request, current_user)
    return order
