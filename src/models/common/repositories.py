import abc

from typing import Generic, List, TypeVar

from .filters import GenericFilter
from .models import GenericModel


Model = TypeVar("Model", bound=GenericModel)
Filter = TypeVar("Filter", bound=GenericFilter)


class GenericRepository(Generic[Model, Filter], metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def get(self, id_: str, /) -> Model:
        """Get entity by ID"""

    @abc.abstractmethod
    async def create(self, model: Model, /) -> Model:
        """Create entity"""

    @abc.abstractmethod
    async def update(self, model: Model, /) -> Model:
        """Update entity"""

    @abc.abstractmethod
    async def list(
        self,
        *,
        limit: int = 100,
        offset: int = 0,
        filters: Filter | None = None,
    ) -> List[Model]:
        """Get list of entities"""

    @abc.abstractmethod
    async def delete(self, id_: str, /) -> None:
        """Delete entity by ID"""
