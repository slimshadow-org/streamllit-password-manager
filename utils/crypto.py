from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

def generate_key(password: str, salt: bytes = None) -> tuple[bytes, bytes]:
    if salt is None:
        salt = os.urandom(16)
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key, salt

def hash_password(password: str) -> dict:
    salt = os.urandom(16)
    key, _ = generate_key(password, salt)
    return {
        "hash": base64.b64encode(key).decode('utf-8'),
        "salt": base64.b64encode(salt).decode('utf-8')
    }

def verify_password(password: str, stored: dict) -> bool:
    salt = base64.b64decode(stored["salt"])
    key, _ = generate_key(password, salt)
    return base64.b64encode(key).decode('utf-8') == stored["hash"]

def get_cipher(key: bytes) -> Fernet:
    return Fernet(key)

def encrypt_data(data: str, key: bytes) -> bytes:
    cipher = get_cipher(key)
    return cipher.encrypt(data.encode())

def decrypt_data(encrypted: bytes, key: bytes) -> str:
    cipher = get_cipher(key)
    return cipher.decrypt(encrypted).decode()