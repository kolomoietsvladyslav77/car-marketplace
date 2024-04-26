from typing import Protocol

from pydantic import BaseModel

from src.interfaces.services.cars import ICarBrandService
from src.models.cars import CarBrandModel

from .dto import ViewBrandDTO


class CreateBrandCommand(BaseModel):
    name: str | None = None


class CreateBrandUseCaseProtocol(Protocol):
    async def __call__(self, cmd: CreateBrandCommand, /) -> ViewBrandDTO:
        """Create brand use case"""


class CreateBrandUseCaseImpl:
    def __init__(
        self,
        car_brand_service: ICarBrandService,
    ):
        self._car_brand_service = car_brand_service

    async def __call__(self, cmd: CreateBrandCommand, /) -> ViewBrandDTO:
        brand = await self._car_brand_service.create_car_brand(
            CarBrandModel(name=cmd.name)
        )

        return ViewBrandDTO(
            id=brand.id,
            name=brand.name,
            created_at=brand.created_at,
            updated_at=brand.updated_at,
        )
