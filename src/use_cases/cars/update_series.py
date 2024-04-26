from typing import Protocol

from pydantic import BaseModel

from src.interfaces.services.cars import ICarBrandService, ICarSeriesService

from .dto import ViewSeriesDTO


class UpdateSeriesCommand(BaseModel):
    id: str
    name: str | None = None
    brand_id: str | None = None


class UpdateSeriesUseCaseProtocol(Protocol):
    async def __call__(self, cmd: UpdateSeriesCommand, /) -> ViewSeriesDTO:
        """Update series use case"""


class UpdateSeriesUseCaseImpl:
    def __init__(
        self,
        car_series_service: ICarSeriesService,
        car_brand_service: ICarBrandService,
    ):
        self._car_series_service = car_series_service
        self._car_brand_service = car_brand_service

    async def __call__(self, cmd: UpdateSeriesCommand, /) -> ViewSeriesDTO:
        series = await self._car_series_service.get_car_series_by_id(cmd.id)

        if name := cmd.name:
            series.name = name

        if brand_id := cmd.brand_id:
            await self._car_brand_service.get_car_brand_by_id(cmd.brand_id)
            series.brand_id = brand_id

        series = await self._car_series_service.update_car_series(series)

        return ViewSeriesDTO(
            id=series.id,
            name=series.name,
            brand_id=series.brand_id,
            created_at=series.created_at,
            updated_at=series.updated_at,
        )
