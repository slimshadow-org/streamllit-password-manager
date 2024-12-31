import json
import os
from datetime import datetime
from typing import List, Optional
from models.password_entry import PasswordEntry
from utils.crypto import encrypt_data, generate_key

class PasswordStore:
    def __init__(self, master_password: str):
        self.file_path = "passwords.enc"
        self.key, self.salt = generate_key(master_password)
        self.entries: List[PasswordEntry] = []
        self._load_entries()

    def _load_entries(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'rb') as f:
                encrypted_data = f.read()
                # Decrypt and load entries
                # Implementation simplified for demonstration
                self.entries = []

    def save_entries(self):
        data = [vars(entry) for entry in self.entries]
        encrypted = encrypt_data(json.dumps(data), self.key)
        with open(self.file_path, 'wb') as f:
            f.write(encrypted)

    def add_entry(self, service: str, username: str, password: str, notes: str = "") -> PasswordEntry:
        entry = PasswordEntry(
            id=os.urandom(16).hex(),
            service=service,
            username=username,
            password=password,
            notes=notes,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        self.entries.append(entry)
        self.save_entries()
        return entry

    def get_entry(self, entry_id: str) -> Optional[PasswordEntry]:
        return next((e for e in self.entries if e.id == entry_id), None)

    def update_entry(self, entry_id: str, **kwargs) -> Optional[PasswordEntry]:
        entry = self.get_entry(entry_id)
        if entry:
            for key, value in kwargs.items():
                if hasattr(entry, key):
                    setattr(entry, key, value)
            entry.updated_at = datetime.now()
            self.save_entries()
        return entry

    def delete_entry(self, entry_id: str) -> bool:
        entry = self.get_entry(entry_id)
        if entry:
            self.entries.remove(entry)
            self.save_entries()
            return True
        return False

    def search_entries(self, query: str) -> List[PasswordEntry]:
        query = query.lower()
        return [
            e for e in self.entries
            if query in e.service.lower() or
               query in e.username.lower() or
               query in e.notes.lower()
        ]