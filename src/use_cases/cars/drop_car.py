from typing import Protocol

from pydantic import BaseModel

from src.interfaces.services.cars import ICarService


class DropCarCommand(BaseModel):
    car_id: str


class DropCarUseCaseProtocol(Protocol):
    async def __call__(self, cmd: DropCarCommand, /) -> None:
        """Drop car use case"""


class DropCarUseCaseImpl:
    def __init__(
        self,
        car_service: ICarService,
    ):
        self._car_service = car_service

    async def __call__(self, cmd: DropCarCommand, /) -> None:
        await self._car_service.delete_car(cmd.car_id)
