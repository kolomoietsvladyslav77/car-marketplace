from typing import Protocol

from pydantic import BaseModel

from src.errors.use_cases.cars import UnsupportedSeriesForCar
from src.interfaces.services.cars import (
    ICarBrandService,
    ICarSeriesService,
    ICarService,
)

from .dto import UpdateCarDTO


class UpdateCarCommand(BaseModel):
    id: str
    brand_id: str | None = None
    model_id: str | None = None
    year: int | None = None
    mileage: int | None = None


class UpdateCarUseCaseProtocol(Protocol):
    async def __call__(self, cmd: UpdateCarCommand, /) -> UpdateCarDTO:
        """Update car use case"""


class UpdateCarUseCaseImpl:
    def __init__(
        self,
        car_service: ICarService,
        car_brand_service: ICarBrandService,
        car_series_service: ICarSeriesService,
    ):
        self._car_service = car_service
        self._car_brand_service = car_brand_service
        self._car_series_service = car_series_service

    async def __call__(self, cmd: UpdateCarCommand, /) -> UpdateCarDTO:
        car = await self._car_service.get_car_by_id(cmd.id)

        car_brand_id = cmd.brand_id or car.brand_id
        car_model_id = cmd.model_id or car.model_id

        model = await self._car_series_service.get_car_series_by_id(
            car_model_id
        )
        if model.brand_id != car_brand_id:
            raise UnsupportedSeriesForCar()

        if brand_id := cmd.brand_id:
            await self._car_brand_service.get_car_brand_by_id(brand_id)
            car.brand_id = brand_id

        if model_id := cmd.model_id:
            await self._car_series_service.get_car_series_by_id(model_id)
            car.model_id = model_id

        if year := cmd.year:
            car.year = year

        if mileage := cmd.mileage:
            car.mileage = mileage

        car = await self._car_service.update_car(car)

        return UpdateCarDTO(
            id=car.id,
            year=car.year,
            mileage=car.mileage,
            user_id=car.user_id,
            created_at=car.created_at,
            updated_at=car.updated_at,
            brand_id=car.brand_id,
            series_id=car.model_id,
        )
