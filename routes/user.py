from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.user import UserSignup, UserLogin
from ..services.auth import signup_user, login_user
from ..database import get_db

router = APIRouter()

@router.post("/signup")
def signup(user: UserSignup, db: Session = Depends(get_db)):
    token = signup_user(db, user.email, user.password)
    return {"token": token}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    token = login_user(db, user.email, user.password)
    if not token:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"token": token}
