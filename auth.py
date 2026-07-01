
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import HTTPException,Depends
from sqlalchemy.orm import Session

from database import get_db
from models import User
from jose import JWTError,jwt

from passlib.context import CryptContext
import random

from datetime import datetime ,timedelta


SECRET_KEY = "change_this_to_long_key_123456"
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7
OTP_EXPIRE_MINUTES = 5


pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
security  = HTTPBearer()


def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(plain,hashed):
    return pwd_context.verify(plain,hashed)

def generate_otp():
    return str(random.randint(100000,999999))

def show_otp(email,otp):
    print("\n" + "=" * 50)
    print("OTP VERIFICATION")
    print("Email:",email)
    print("OTP",otp)
    print("\n" + "=" * 50)

def create_access_token(data:dict):
    payload = data.copy()
    payload.update({
        "exp": datetime.utcnow()+ timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES),
        "type" : "access"
    })
    return jwt.encode(payload, SECRET_KEY, algorithm= ALGORITHM)


def create_refresh_token(data: dict):
    payload = data.copy()
    payload.update({
        "exp": datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS),
        "type": "refresh"
    })
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token:str, expected_type :str):
    try:
        payload =jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        if payload.get("type") != expected_type:
            raise HTTPException(401,"Invalid token type")
        return payload
    except JWTError :
        raise HTTPException(401,"Invalid or expired token")
    
def get_current_user(
        credentials :HTTPAuthorizationCredentials = Depends(security),
        db: Session = Depends(get_db)
):
    token = credentials.credentials
    payload = decode_token(token,"access")
    username = payload.get("sub")
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(404,"User not found")
    return user

def admin_required(current_user :User =Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(403,"Admin only")
    return current_user



def check_deleted(user:User):
    if user.is_deleted:
        raise HTTPException (403,"Account is deactivated")



    

    