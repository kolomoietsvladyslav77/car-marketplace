from typing import Protocol

from pydantic import BaseModel

from src.interfaces.services.cars import (
    ICarBrandService,
    ICarSeriesService,
    ICarService,
)

from .dto import SeriesDTO, ViewBrandDTO, ViewCarDTO


class ViewCarCommand(BaseModel):
    car_id: str


class ViewCarUseCaseProtocol(Protocol):
    async def __call__(self, cmd: ViewCarCommand, /) -> ViewCarDTO:
        """View car use case"""


class ViewCarUseCaseImpl:
    def __init__(
        self,
        car_service: ICarService,
        car_brand_service: ICarBrandService,
        car_series_service: ICarSeriesService,
    ):
        self._car_service = car_service
        self._car_brand_service = car_brand_service
        self._car_series_service = car_series_service

    async def __call__(self, cmd: ViewCarCommand, /) -> ViewCarDTO:
        car = await self._car_service.get_car_by_id(cmd.car_id)
        series = await self._car_series_service.get_car_series_by_id(
            car.model_id
        )
        brand = await self._car_brand_service.get_car_brand_by_id(car.brand_id)

        return ViewCarDTO(
            id=car.id,
            year=car.year,
            mileage=car.mileage,
            user_id=car.user_id,
            created_at=car.created_at,
            updated_at=car.updated_at,
            brand=ViewBrandDTO(
                id=brand.id,
                name=brand.name,
                created_at=brand.created_at,
                updated_at=brand.updated_at,
            ),
            series=SeriesDTO(
                id=series.id,
                name=series.name,
                created_at=series.created_at,
                updated_at=series.updated_at,
            ),
        )
