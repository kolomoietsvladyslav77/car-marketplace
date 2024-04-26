import datetime

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class ViewUserDTO:
    id: str
    email: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


@dataclass(frozen=True)
class ViewUsersDTO:
    users: List[ViewUserDTO]
