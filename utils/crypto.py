from passlib.context import CryptContext


class Crypto:
    def __init__(self) -> None:
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def encrypt(self, password: str) -> str:
        return self.pwd_context.hash(password)
    
    def verify(self, password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(password, hashed_password)