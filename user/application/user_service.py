from ulid import ULID
from fastapi import HTTPException
from user.domain.repository.user_repo import IUserRepository
from user.infra.repository.user_repo import UserRepository
from user.domain.user import User
from datetime import datetime
from utils.crypto import Crypto

class UserService:
    def __init__(self) -> None:
        self.user_repo: IUserRepository = UserRepository()
        self.ulid = ULID()
        self.crypto = Crypto()
        
    def create_user(self, name: str, email: str, password: str) -> User:
        _user = None 
        
        try:
            _user = self.user_repo.find_by_email(email)
        except HTTPException as e:
            if e.status_code != 422:
                raise e  
        
        if _user:
            raise HTTPException(status_code=422)
        
        password: str = self.crypto.encrypt(password)
        now = datetime.now()
        user: User = User(
            id=self.ulid.to_uuid(),
            name=name,
            email=email,
            password=password,
            created_at=now,
            updated_at=now
        )
        
        self.user_repo.save(user)
        
        return user 