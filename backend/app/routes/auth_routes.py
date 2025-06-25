from fastapi import APIRouter, HTTPException
from app.models.schemas import UserRegister, UserLogin
from app.db import users_collection
from app.auth import hash_password, verify_password, create_access_token
from fastapi import APIRouter
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
def login_user(user: UserLogin):
    db_user = users_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.email})
    return {"access_token": token}
