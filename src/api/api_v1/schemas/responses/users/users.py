import datetime

from typing import List

from pydantic import BaseModel


class UsersResponseSchema(BaseModel):
    id: str
    email: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class ListUsersResponseSchema(BaseModel):
    users: List[UsersResponseSchema]
