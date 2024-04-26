import abc

from src.models.common.repositories import GenericRepository

from .filters import CarBrandFilter, CarFilter, CarSeriesFilter
from .models import CarBrandModel, CarModel, CarSeriesModel


class ICarRepository(
    GenericRepository[CarModel, CarFilter], metaclass=abc.ABCMeta
):
    """Repository for CarModel entity"""

    @abc.abstractmethod
    async def delete_by_user_id(self, user_id: str) -> None:
        """Delete car by user id"""


class ICarBrandRepository(
    GenericRepository[CarBrandModel, CarBrandFilter], metaclass=abc.ABCMeta
):
    """Repository for CarBrandModel entity"""

    @abc.abstractmethod
    async def get_by_car_id(self, car_id: str) -> CarModel:
        """Get car brands by id car_id"""


class ICarSeriesRepository(
    GenericRepository[CarSeriesModel, CarSeriesFilter], metaclass=abc.ABCMeta
):
    """Repository for CarSeriesModel entity"""

    @abc.abstractmethod
    async def get_by_car_id(self, car_id: str) -> CarModel:
        """Get car series by id car_id"""
