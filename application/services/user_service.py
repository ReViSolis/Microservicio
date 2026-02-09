from typing import Optional, List
from application.ports.user_repository import UserRepository
from domain.user import User, UserCreate, UserUpdate

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register_user(self, user_data: UserCreate) -> User:
        # Validación de negocio
        if not user_data.nombre or not user_data.email:
            raise ValueError("nombre and email are required")

        # Verificar unicidad del email
        existing_user = self.repository.find_by_email(user_data.email)
        if existing_user:
            raise ValueError(f"Email {user_data.email} is already registered")

        return self.repository.save(user_data)

    def get_user(self, user_id: int) -> Optional[User]:
        return self.repository.find_by_id(user_id)

    def get_all_users(self) -> List[User]:
        return self.repository.find_all()

    def update_user(self, user_id: int, user_update: UserUpdate) -> Optional[User]:
        user = self.repository.find_by_id(user_id)
        if not user:
            return None

        # Validar que el nuevo email no esté en uso por otro usuario
        if user_update.email is not None and user_update.email != user.email:
            existing_user = self.repository.find_by_email(user_update.email)
            if existing_user:
                raise ValueError(f"Email {user_update.email} is already in use")

        return self.repository.update(user_id, user_update)

    def delete_user(self, user_id: int) -> bool:
        return self.repository.delete(user_id)