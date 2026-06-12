from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

class UserRole(Enum):
    ADMIN   = "Admin"
    STUDENT = "Student"

@dataclass
class User:
    user_id:       str
    password_hash: str
    role:          UserRole
    name:          Optional[str]      = None
    email:         Optional[str]      = None
    is_active:     bool               = True
    created_at:    Optional[datetime] = None

    @property
    def is_admin(self) -> bool:
        return self.role == UserRole.ADMIN

    @property
    def is_student(self) -> bool:
        return self.role == UserRole.STUDENT

    @property
    def display_name(self) -> str:
        return self.name or self.user_id

    def to_dict(self) -> dict:
        return {
            "user_id":   self.user_id,
            "name":      self.name,
            "email":     self.email,
            "role":      self.role.value,
            "is_active": self.is_active,
        }

    def __str__(self) -> str:
        return f"{self.display_name} ({self.role.value})"