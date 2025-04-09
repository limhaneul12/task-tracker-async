from abc import ABCMeta, abstractmethod
from user.domain.user import User

class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, user: User) -> User:
        raise NotImplementedError
    
    
    @abstractmethod
    def find_by_email(self, email: str) -> User:
        """이메일로 유저 조회 없으면 422"""
        raise NotImplementedError