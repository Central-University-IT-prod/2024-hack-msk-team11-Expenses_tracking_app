from pydantic import BaseModel
from backend.src.shemas.users import UserRead


class Auth(BaseModel):
    username: str
    password: str


class AuthResponse(BaseModel):
    token: str
    type: str = "Bearer"


class UserRegisterResponse(BaseModel):
    user: UserRead
    auth: AuthResponse
