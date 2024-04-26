from typing import Protocol

from pydantic import BaseModel

from src.interfaces.services.users import IUserService

from .dto import ViewUserDTO


class ViewUserCommand(BaseModel):
    user_id: str


class ViewUserUseCaseProtocol(Protocol):
    async def __call__(self, cmd: ViewUserCommand, /) -> ViewUserDTO:
        """Sign in use case"""


class ViewUserUseCaseImpl:
    def __init__(
        self,
        user_service: IUserService,
    ):
        self._user_service = user_service

    async def __call__(self, cmd: ViewUserCommand, /) -> ViewUserDTO:
        user = await self._user_service.get_user_by_id(cmd.user_id)
        return ViewUserDTO(
            email=user.email,
            id=user.id,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )
