from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import hash_password, verify_password, create_access_token
from app.db import users_collection
from app.models.schemas import UserRegister
from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    password: str
router = APIRouter()

@router.post("/register")
def register_user(user: UserRegister):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already exists")
    hashed_pwd = hash_password(user.password)
    users_collection.insert_one({
        "username": user.username,
        "email": user.email,
        "password": hashed_pwd
    })
    return {"message": "User registered successfully"}

@router.post("/login")
def login_user(request: LoginRequest):
    db_user = users_collection.find_one({"email": request.email})
    if not db_user or not verify_password(request.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": db_user["email"]})
    return {
        "access_token": token,
        "token_type": "bearer"
    }