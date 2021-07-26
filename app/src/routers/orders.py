from fastapi import Depends, APIRouter
from ..lib.schemas import User
from ..lib.dependencies import get_current_user

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)


@router.post("")
async def add_order(current_user: User = Depends(get_current_user)):
    print(current_user)
    return "OK"
