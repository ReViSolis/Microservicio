from abc import ABC, abstractmethod
from typing import Optional, List
from domain.user import User, UserCreate, UserUpdate

class UserRepository(ABC):
    @abstractmethod
    def save(self, user_data: UserCreate) -> User: ...

    @abstractmethod
    def find_by_id(self, user_id: int) -> Optional[User]: ...

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]: ...

    @abstractmethod
    def find_all(self) -> List[User]: ...

    @abstractmethod
    def update(self, user_id: int, user_update: UserUpdate) -> Optional[User]: ...

    @abstractmethod
    def delete(self, user_id: int) -> bool: ...