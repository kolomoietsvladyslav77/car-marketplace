from pydantic import BaseModel


class RefreshRequestSchema(BaseModel):
    token: str
