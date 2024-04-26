from typing import Protocol

from pydantic import BaseModel

from src.interfaces.services.cars import ICarBrandService

from .dto import ViewBrandDTO, ViewBrandsDTO


class ViewBrandCommand(BaseModel):
    pass


class ViewBrandUseCaseProtocol(Protocol):
    async def __call__(self, cmd: ViewBrandCommand, /) -> ViewBrandsDTO:
        """View brands use case"""


class ViewBrandUseCaseImpl:
    def __init__(
        self,
        car_brand_service: ICarBrandService,
    ):
        self._car_brand_service = car_brand_service

    async def __call__(self, cmd: ViewBrandCommand, /) -> ViewBrandsDTO:
        brands = await self._car_brand_service.list_car_brands()
        result_brands = [
            ViewBrandDTO(
                id=brand.id,
                name=brand.name,
                created_at=brand.created_at,
                updated_at=brand.updated_at,
            )
            for brand in brands
        ]
        return ViewBrandsDTO(brands=result_brands)
