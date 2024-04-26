from typing import Protocol

from pydantic import BaseModel

from src.errors.use_cases.cars import UnsupportedSeriesForCar
from src.interfaces.services.cars import (
    ICarBrandService,
    ICarSeriesService,
    ICarService,
)
from src.models.cars import CarModel

from .dto import SeriesDTO, ViewBrandDTO, ViewCarDTO


class CreateCarCommand(BaseModel):
    brand_id: str
    model_id: str
    year: int
    mileage: int
    user_id: str


class CreateCarUseCaseProtocol(Protocol):
    async def __call__(self, cmd: CreateCarCommand, /) -> ViewCarDTO:
        """Create car use case"""


class CreateCarUseCaseImpl:
    def __init__(
        self,
        car_service: ICarService,
        car_brand_service: ICarBrandService,
        car_series_service: ICarSeriesService,
    ):
        self._car_service = car_service
        self._car_brand_service = car_brand_service
        self._car_series_service = car_series_service

    async def __call__(self, cmd: CreateCarCommand, /) -> ViewCarDTO:
        brand = await self._car_brand_service.get_car_brand_by_id(cmd.brand_id)
        series = await self._car_series_service.get_car_series_by_id(
            cmd.model_id
        )

        if series.brand_id != brand.id:
            raise UnsupportedSeriesForCar()

        car = await self._car_service.create_car(
            CarModel(
                brand_id=brand.id,
                model_id=series.id,
                year=cmd.year,
                mileage=cmd.mileage,
                user_id=cmd.user_id,
            )
        )

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
