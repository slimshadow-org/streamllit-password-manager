from dataclasses import dataclass
from datetime import datetime

@dataclass
class PasswordEntry:
    id: str
    service: str
    username: str
    password: str
    notes: str
    created_at: datetime
    updated_at: datetime