from fastapi import APIRouter
from pydantic import BaseModel

from user.application.user_service import UserService

router = APIRouter(prefix="/users")


class CreateUserBody(BaseModel):
    name: str
    email: str
    password: str


@router.post("")
async def create_user(user: CreateUserBody):
    user_service = UserService()
    created_user = user_service.create_user(user.name, user.email, user.password)
    return created_user
    