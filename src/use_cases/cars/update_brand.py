from typing import Protocol

from pydantic import BaseModel

from src.interfaces.services.cars import ICarBrandService

from .dto import ViewBrandDTO


class UpdateBrandCommand(BaseModel):
    id: str | None = None
    name: str | None = None


class UpdateBrandUseCaseProtocol(Protocol):
    async def __call__(self, cmd: UpdateBrandCommand, /) -> ViewBrandDTO:
        """Update brand use case"""


class UpdateBrandUseCaseImpl:
    def __init__(
        self,
        car_brand_service: ICarBrandService,
    ):
        self._car_brand_service = car_brand_service

    async def __call__(self, cmd: UpdateBrandCommand, /) -> ViewBrandDTO:
        brand = await self._car_brand_service.get_car_brand_by_id(cmd.id)

        if name := cmd.name:
            brand.name = name

        brand = await self._car_brand_service.update_car_brand(brand)

        return ViewBrandDTO(
            id=brand.id,
            name=brand.name,
            created_at=brand.created_at,
            updated_at=brand.updated_at,
        )
