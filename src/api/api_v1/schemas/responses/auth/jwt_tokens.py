from pydantic import BaseModel


class JWTTokensResponseSchema(BaseModel):
    access_token: str
    refresh_token: str
