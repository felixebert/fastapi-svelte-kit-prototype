from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from ..lib.crypt import verify_password, create_access_token
from ..lib.database import get_user

router = APIRouter()


class Token(BaseModel):
    access_token: str
    token_type: str


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if user is None:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
