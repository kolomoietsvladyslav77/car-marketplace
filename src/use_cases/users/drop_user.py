from typing import Protocol

from pydantic import BaseModel

from src.interfaces.services.cars import ICarService
from src.interfaces.services.users import IUserService


class DropUserCommand(BaseModel):
    user_id: str


class DropUserUseCaseProtocol(Protocol):
    async def __call__(self, cmd: DropUserCommand, /) -> None:
        """Sign in use case"""


class DropUserUseCaseImpl:
    def __init__(
        self,
        user_service: IUserService,
        car_service: ICarService,
    ):
        self._user_service = user_service
        self._car_service = car_service

    async def __call__(self, cmd: DropUserCommand, /) -> None:
        await self._car_service.delete_cars_by_user_id(cmd.user_id)
        await self._user_service.delete_user(cmd.user_id)
