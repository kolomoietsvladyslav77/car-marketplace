import abc

from typing import List

from src.models.cars import CarBrandModel, CarModel, CarSeriesModel


class ICarService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def get_car_by_id(self, car_id: str) -> CarModel:
        """Retrieve a car by its ID."""

    @abc.abstractmethod
    async def update_car(self, car: CarModel) -> CarModel:
        """Update a car's details in the database."""

    @abc.abstractmethod
    async def create_car(self, car: CarModel) -> CarModel:
        """Create a new car in the database."""

    @abc.abstractmethod
    async def list_cars(
        self, limit: int | None = None, offset: int | None = None
    ) -> List[CarModel]:
        """List cars with optional pagination."""

    @abc.abstractmethod
    async def delete_car(self, car_id: str) -> None:
        """Delete a car by its ID."""

    @abc.abstractmethod
    async def delete_cars_by_user_id(self, user_id: int) -> None:
        """Delete cars by user id"""


class ICarBrandService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def get_car_brand_by_id(self, car_brand_id: str) -> CarBrandModel:
        """Retrieve a car brand by its ID."""

    @abc.abstractmethod
    async def update_car_brand(
        self, car_brand: CarBrandModel
    ) -> CarBrandModel:
        """Update a car brand's details in the database."""

    @abc.abstractmethod
    async def create_car_brand(
        self, car_brand: CarBrandModel
    ) -> CarBrandModel:
        """Create a new car brand in the database."""

    @abc.abstractmethod
    async def list_car_brands(
        self, limit: int | None = None, offset: int | None = None
    ) -> List[CarBrandModel]:
        """List car brands with optional pagination."""

    @abc.abstractmethod
    async def delete_car_brand(self, car_brand_id: str) -> None:
        """Delete a car brand from the database."""

    @abc.abstractmethod
    async def list_by_car_id(self, car_id: str) -> List[CarBrandModel]:
        """List car brands by car id."""


class ICarSeriesService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def get_car_series_by_id(self, car_series_id: str) -> CarSeriesModel:
        """Retrieve a car series by its ID."""

    @abc.abstractmethod
    async def update_car_series(
        self, car_series: CarSeriesModel
    ) -> CarSeriesModel:
        """Update a car series' details in the database."""

    @abc.abstractmethod
    async def create_car_series(
        self, car_series: CarSeriesModel
    ) -> CarSeriesModel:
        """Create a new car series in the database."""

    @abc.abstractmethod
    async def list_car_series(
        self, limit: int | None = None, offset: int | None = None
    ) -> List[CarSeriesModel]:
        """List car series with optional pagination."""

    @abc.abstractmethod
    async def delete_car_series(self, car_series_id: str) -> None:
        """Delete a car series from the database."""

    @abc.abstractmethod
    async def list_by_car_id(self, car_id: str) -> List[CarBrandModel]:
        """List car series by car id."""
