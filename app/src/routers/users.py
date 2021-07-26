from fastapi import Depends, APIRouter
from ..lib.schemas import User
from ..lib.dependencies import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
