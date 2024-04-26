from typing import Protocol

from pydantic import BaseModel

from src.interfaces.services.cars import (
    ICarBrandService,
    ICarSeriesService,
    ICarService,
)

from .dto import SeriesDTO, ViewBrandDTO, ViewCarDTO, ViewCarsDTO


class ViewCarsCommand(BaseModel):
    pass


class ViewCarsUseCaseProtocol(Protocol):
    async def __call__(self, cmd: ViewCarsCommand, /) -> ViewCarsDTO:
        """View cars use case"""


class ViewCarsUseCaseImpl:
    def __init__(
        self,
        car_service: ICarService,
        car_brand_service: ICarBrandService,
        car_series_service: ICarSeriesService,
    ):
        self._car_service = car_service
        self._car_brand_service = car_brand_service
        self._car_series_service = car_series_service

    async def __call__(self, cmd: ViewCarsCommand, /) -> ViewCarsDTO:
        result_cars = list()

        cars = await self._car_service.list_cars()
        for car in cars:
            series = await self._car_series_service.get_car_series_by_id(
                car.model_id
            )
            brand = await self._car_brand_service.get_car_brand_by_id(
                car.brand_id
            )

            result_cars.append(
                ViewCarDTO(
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
            )
        return ViewCarsDTO(cars=result_cars)
