from enum import Enum
from typing import Optional
from pydantic import BaseModel

class UserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class User(BaseModel):
    idusuario: int
    nombre: str
    email: str
    status: UserStatus = UserStatus.ACTIVE
    class Config:
        json_schema_extra = {
            "example": {
                "idusuario": 1,
                "nombre": "Sergio Pérez",
                "email": "sergio@example.com",
                "status": "active",
                "created_at": "2024-01-15T10:30:00"
            }
            
        }

class UserCreate(BaseModel):
    Usuario: str
    email: str
    idusuario: Optional[int] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "Usuario": "Juan Pérez",
                "email": "juan@example.com",
                "idusuario": 12345
            }
        }

class UserUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    status: Optional[UserStatus] = None