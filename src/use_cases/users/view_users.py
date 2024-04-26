from typing import Protocol

from pydantic import BaseModel

from src.interfaces.services.users import IUserService

from .dto import ViewUserDTO, ViewUsersDTO


class ViewUsersCommand(BaseModel):
    pass


class ViewUsersUseCaseProtocol(Protocol):
    async def __call__(self, cmd: ViewUsersCommand, /) -> ViewUsersDTO:
        """Sign in use case"""


class ViewUsersUseCaseImpl:
    def __init__(
        self,
        user_service: IUserService,
    ):
        self._user_service = user_service

    async def __call__(self, cmd: ViewUsersCommand, /) -> ViewUsersDTO:
        users = await self._user_service.list_users()
        users_dto = [
            ViewUserDTO(
                email=user.email,
                id=user.id,
                created_at=user.created_at,
                updated_at=user.updated_at,
            )
            for user in users
        ]
        return ViewUsersDTO(users=users_dto)
