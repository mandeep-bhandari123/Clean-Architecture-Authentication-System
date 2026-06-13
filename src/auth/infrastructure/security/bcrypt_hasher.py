from bcrypt import hashpw, checkpw, gensalt
from src.auth.application.ports.password_hasher import AbstractPasswordHasher

class BcryptPasswordHasher(AbstractPasswordHasher):

    def hash(self, plain_password: str) -> str:
        return hashpw(plain_password.encode(), gensalt()).decode()

    def verify(self, plain_password: str, hashed_password: str) -> bool:
        return checkpw(plain_password.encode(), hashed_password.encode())
