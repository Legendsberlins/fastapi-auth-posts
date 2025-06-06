import bcrypt
import secrets
from sqlalchemy.orm import Session
from ..models.user import User

def signup_user(db: Session, email: str, password: str):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    user = User(email=email, password=hashed_password, token=secrets.token_hex(16))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user.token

def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return user.token
    return None

def validate_token(db: Session, token: str):
    return db.query(User).filter(User.token == token).first()

