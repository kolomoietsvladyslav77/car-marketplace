from typing import Protocol

from pydantic import BaseModel

from src.interfaces.services.cars import ICarBrandService, ICarSeriesService
from src.models.cars import CarSeriesModel

from .dto import ViewSeriesDTO


class CreateSeriesCommand(BaseModel):
    name: str | None = None
    brand_id: str | None = None


class CreateSeriesUseCaseProtocol(Protocol):
    async def __call__(self, cmd: CreateSeriesCommand, /) -> ViewSeriesDTO:
        """Create car use case"""


class CreateSeriesUseCaseImpl:
    def __init__(
        self,
        car_series_service: ICarSeriesService,
        car_brand_service: ICarBrandService,
    ):
        self._car_series_service = car_series_service
        self._car_brand_service = car_brand_service

    async def __call__(self, cmd: CreateSeriesCommand, /) -> ViewSeriesDTO:
        brand = await self._car_brand_service.get_car_brand_by_id(cmd.brand_id)
        series = await self._car_series_service.create_car_series(
            CarSeriesModel(
                name=cmd.name,
                brand_id=brand.id,
            )
        )

        return ViewSeriesDTO(
            id=series.id,
            name=series.name,
            brand_id=series.brand_id,
            created_at=series.created_at,
            updated_at=series.updated_at,
        )
