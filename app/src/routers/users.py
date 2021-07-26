from fastapi import Depends, APIRouter, Response
from ..lib.schemas import User
from ..lib.dependencies import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("/me")
async def read_users_me(response: Response, current_user: User = Depends(get_current_user)):
    response.headers["Cache-Control"] = "no-cache, max-age=0"
    return current_user
