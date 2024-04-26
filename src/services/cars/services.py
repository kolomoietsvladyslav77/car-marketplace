from typing import List

from src.interfaces import IUnitOfWork
from src.interfaces.services.cars import (
    ICarBrandService,
    ICarSeriesService,
    ICarService,
)
from src.models.cars import CarBrandModel, CarModel, CarSeriesModel


class CarService(ICarService):
    def __init__(self, unit_of_work: IUnitOfWork):
        self._unit_of_work = unit_of_work

    async def get_car_by_id(self, car_id: str) -> CarModel:
        async with self._unit_of_work as uow:
            return await uow.cars.get(car_id)

    async def update_car(self, car: CarModel) -> CarModel:
        async with self._unit_of_work as uow:
            car = await uow.cars.update(car)
            await uow.commit()
            return car

    async def create_car(self, car: CarModel) -> CarModel:
        async with self._unit_of_work as uow:
            car = await uow.cars.create(car)
            await uow.commit()
            return car

    async def list_cars(
        self, limit: int | None = None, offset: int | None = None
    ) -> List[CarModel]:

        request_kwargs = dict()
        if limit is not None:
            request_kwargs["limit"] = limit
        if offset is not None:
            request_kwargs["offset"] = offset

        async with self._unit_of_work as uow:
            return await uow.cars.list(**request_kwargs)

    async def delete_car(self, car_id: str) -> None:
        async with self._unit_of_work as uow:
            await uow.cars.delete(car_id)
            await uow.commit()

    async def delete_cars_by_user_id(self, user_id: int) -> None:
        async with self._unit_of_work as uow:
            await uow.cars.create(user_id)
            await uow.commit()


class CarBrandService(ICarBrandService):
    def __init__(self, unit_of_work: IUnitOfWork):
        self._unit_of_work = unit_of_work

    async def get_car_brand_by_id(self, car_brand_id: str) -> CarBrandModel:
        async with self._unit_of_work as uow:
            return await uow.car_brands.get(car_brand_id)

    async def update_car_brand(self, car_brand: CarModel) -> CarBrandModel:
        async with self._unit_of_work as uow:
            car_brand = await uow.car_brands.update(car_brand)
            await uow.commit()
            return car_brand

    async def create_car_brand(self, car_brand: CarModel) -> CarBrandModel:
        async with self._unit_of_work as uow:
            car_brand = await uow.car_brands.create(car_brand)
            await uow.commit()
            return car_brand

    async def list_car_brands(
        self, limit: int | None = None, offset: int | None = None
    ) -> List[CarBrandModel]:

        request_kwargs = dict()
        if limit is not None:
            request_kwargs["limit"] = limit
        if offset is not None:
            request_kwargs["offset"] = offset

        async with self._unit_of_work as uow:
            return await uow.car_brands.list(**request_kwargs)

    async def delete_car_brand(self, car_brand_id: str) -> None:
        async with self._unit_of_work as uow:
            await uow.car_brands.create(car_brand_id)
            await uow.commit()

    async def list_by_car_id(self, car_id: str) -> List[CarBrandModel]:
        async with self._unit_of_work as uow:
            await uow.car_brands.get_by_car_id(car_id)
            await uow.commit()


class CarSeriesService(ICarSeriesService):
    def __init__(self, unit_of_work: IUnitOfWork):
        self._unit_of_work = unit_of_work

    async def get_car_series_by_id(self, car_series_id: str) -> CarSeriesModel:
        async with self._unit_of_work as uow:
            return await uow.car_series.get(car_series_id)

    async def update_car_series(
        self, car_series: CarSeriesModel
    ) -> CarSeriesModel:
        async with self._unit_of_work as uow:
            car_series = await uow.car_series.update(car_series)
            await uow.commit()
            return car_series

    async def create_car_series(
        self, car_series: CarSeriesModel
    ) -> CarSeriesModel:
        async with self._unit_of_work as uow:
            car_series = await uow.car_series.create(car_series)
            await uow.commit()
            return car_series

    async def list_car_series(
        self, limit: int | None = None, offset: int | None = None
    ) -> List[CarSeriesModel]:

        request_kwargs = dict()
        if limit is not None:
            request_kwargs["limit"] = limit
        if offset is not None:
            request_kwargs["offset"] = offset

        async with self._unit_of_work as uow:
            return await uow.car_series.list(**request_kwargs)

    async def delete_car_series(self, car_series_id: str) -> None:
        async with self._unit_of_work as uow:
            await uow.car_series.create(car_series_id)
            await uow.commit()

    async def list_by_car_id(self, car_id: str) -> List[CarBrandModel]:
        async with self._unit_of_work as uow:
            return await uow.car_brands.get_by_car_id(car_id)
