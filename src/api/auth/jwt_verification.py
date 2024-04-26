from typing import Tuple

from fastapi import HTTPException
from fastapi.requests import Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError

from .utils import decode_jwt


class JWTVerificationService(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(
            request
        )
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )
            is_valid, user_id = self.verify_jwt(credentials.credentials)
            if not is_valid:
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token."
                )
            return user_id
        else:
            raise HTTPException(
                status_code=403, detail="Invalid authorization code."
            )

    @staticmethod
    def verify_jwt(jwt_token: str) -> Tuple[bool, str | None]:
        is_token_valid: bool = False

        user_id = None
        try:
            payload = decode_jwt(jwt_token)
            user_id = payload.get("sub")
        except JWTError:
            payload = None
        if payload:
            is_token_valid = True

        return is_token_valid, user_id
