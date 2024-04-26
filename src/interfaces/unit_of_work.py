import abc

from typing import Optional, Type

from typing_extensions import Self

from src.models.cars import (
    ICarBrandRepository,
    ICarRepository,
    ICarSeriesRepository,
)
from src.models.users import IUserRepository


class IUnitOfWork:
    users: IUserRepository
    cars: ICarRepository
    car_brands: ICarBrandRepository
    car_series: ICarSeriesRepository

    @abc.abstractmethod
    def __init__(self, storage):
        """Initialize repository"""

    @abc.abstractmethod
    async def __aenter__(self) -> Self:
        """Async context"""

    @abc.abstractmethod
    async def __aexit__(
        self,
        exc_type: Optional[Type[Exception]],
        exc_val: Optional[Exception],
        traceback,
    ):
        """Async close context"""

    @abc.abstractmethod
    async def commit(self):
        """Commit transaction"""

    @abc.abstractmethod
    async def rollback(self):
        """Rollback transaction"""

    @property
    @abc.abstractmethod
    def engine(self):
        """Get storage engine"""

    @property
    @abc.abstractmethod
    def session(self):
        """Get storage session"""
