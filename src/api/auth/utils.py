import os

from fastapi import FastAPI
from fastapi.security import HTTPBearer
from jose import jwt


app = FastAPI()
security = HTTPBearer()

ALGORITHM = "HS256"

SECRET_KEY = os.environ["SUPABASE_SECRET_JWT_KEY"]


def decode_jwt(token: str) -> dict:
    return jwt.decode(
        token, SECRET_KEY, algorithms=[ALGORITHM], audience="authenticated"
    )
