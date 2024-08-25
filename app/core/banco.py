from app.api.models.usuario import UsuarioDB
from typing import Optional, List

class Bank:
    def __init__(self):
        self.clients: List[Client] = []
        self.accounts: List[Account] = []
        self.users: List[UsuarioDB] = []

    def register_user(self, username: str, hashed_password: str) -> UsuarioDB:
        user = UsuarioDB(username=username, hashed_password=hashed_password)
        self.users.append(user)
        return user

    def find_user_by_username(self, username: str) -> Optional[UsuarioDB]:
        for user in self.users:
            if user.username == username:
                return user
        return None
