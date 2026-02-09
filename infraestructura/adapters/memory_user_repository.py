from typing import Optional, List
from application.ports.user_repository import UserRepository
from domain.user import User, UserCreate, UserUpdate, UserStatus

class MemoryUserRepository(UserRepository):
    def __init__(self):
        self.users: dict[int, User] = {}
        self.next_id = 1

    def save(self, user_data: UserCreate) -> User:
        user = User(
            idusuario=self.next_id,
            nombre=user_data.nombre,
            email=user_data.email,
            status=UserStatus.ACTIVE
        )
        self.users[self.next_id] = user
        self.next_id += 1
        return user

    def find_by_id(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id)

    def find_by_email(self, email: str) -> Optional[User]:
        for u in self.users.values():
            if u.email == email:
                return u
        return None

    def find_all(self) -> List[User]:
        return list(self.users.values())

    def update(self, user_id: int, user_update: UserUpdate) -> Optional[User]:
        user = self.find_by_id(user_id)
        if not user:
            return None
        changes = {k: v for k, v in user_update.model_dump().items() if v is not None}
        new_user = user.model_copy(update=changes)
        self.users[user_id] = new_user
        return new_user

    def delete(self, user_id: int) -> bool:
        return self.users.pop(user_id, None) is not None