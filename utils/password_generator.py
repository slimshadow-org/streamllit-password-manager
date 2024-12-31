import string
import secrets

def generate_password(length: int = 16) -> str:
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

def check_password_strength(password: str) -> tuple[int, str]:
    score = 0
    feedback = []
    
    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Password should be at least 12 characters long")
        
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Include uppercase letters")
        
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Include lowercase letters")
        
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include numbers")
        
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Include special characters")
        
    return score, "\n".join(feedback) if feedback else "Strong password!"