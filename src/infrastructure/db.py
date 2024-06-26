from asyncio import current_task
from contextlib import asynccontextmanager
from typing import Callable

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_scoped_session,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker


class AsyncSQLAlchemy:
    def __init__(self, db_uri: str) -> None:
        self._db_uri = db_uri
        self._engine: AsyncEngine = None
        self._session_factory = None

        self._engine = create_async_engine(self._db_uri)

    async def disconnect(self):
        await self._engine.dispose()

    def init_session_factory(
        self, autocommit: bool = False, autoflush: bool = False
    ):
        self._session_factory = async_scoped_session(
            sessionmaker(
                autocommit=autocommit,
                autoflush=autoflush,
                bind=self._engine,
                class_=AsyncSession,
            ),
            scopefunc=current_task,
        )

    @asynccontextmanager
    async def session(self) -> Callable[..., AsyncSession]:
        assert self._session_factory is not None

        session: AsyncSession = self._session_factory()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

    async def get_db_session(self) -> Callable[..., AsyncSession]:
        assert self._session_factory is not None

        session: AsyncSession = self._session_factory()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

    @property
    def engine(self):
        assert self._engine is not None
        return self._engine

    @property
    def session_factory(self):
        assert self._session_factory is not None
        return self._session_factory
