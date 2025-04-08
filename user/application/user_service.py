from ulid import ULID
from datetime import datetime
from user.domain.user import User
from user.domain.repository.user_repo import IUserRepository
from user.infra.repository.user_repo import UserRepository



class UserService:
    def __init__(self) -> None:
        self.user_repo: IUserRepository = UserRepository()
        self.ulid = ULID()