from typing import Optional, Type

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from typing_extensions import Self

from src.infrastructure.db import AsyncSQLAlchemy
from src.infrastructure.repositories.cars import (
    SQLAlchemyCarBrandRepository,
    SQLAlchemyCarRepository,
    SQLAlchemyCarSeriesRepository,
)
from src.infrastructure.repositories.users import SQLAlchemyUserRepository
from src.interfaces.unit_of_work import IUnitOfWork


class SQLAlchemyUnitOfWork(IUnitOfWork):
    def __init__(self, storage: AsyncSQLAlchemy):
        self._storage = storage

    async def __aenter__(self) -> Self:
        self._storage.init_session_factory()
        self._session = self._storage.session_factory()

        self.users: SQLAlchemyUserRepository = SQLAlchemyUserRepository(
            session=self._session
        )
        self.cars: SQLAlchemyCarRepository = SQLAlchemyCarRepository(
            session=self._session,
        )
        self.car_brands: SQLAlchemyCarBrandRepository = (
            SQLAlchemyCarBrandRepository(
                session=self._session,
            )
        )
        self.car_series: SQLAlchemyCarSeriesRepository = (
            SQLAlchemyCarSeriesRepository(
                session=self._session,
            )
        )

        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[Exception]],
        exc_val: Optional[Exception],
        traceback,
    ):
        if exc_type:
            await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self._session.rollback()

    @property
    def engine(self) -> AsyncEngine:
        assert self._storage is not None
        return self._storage.engine

    @property
    def session(self) -> AsyncSession:
        assert self._session is not None
        return self._session
