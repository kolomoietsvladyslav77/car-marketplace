from typing import List

from sqlalchemy import delete, insert, select, update

from src.errors.repository import UserNotFound
from src.infrastructure.repositories.common import GenericSQLAlchemyRepository
from src.infrastructure.tables.users import UserTable
from src.models.users import IUserRepository, UserFilter, UserModel


class SQLAlchemyUserRepository(IUserRepository, GenericSQLAlchemyRepository):
    async def get_by_super_id(self, id_: int, /) -> UserModel:
        stmt = select(UserTable).where(UserTable.super_id == id_)
        res = await self._session.execute(stmt)
        if user := res.fetchone():
            return user.to_read_model()
        raise UserNotFound()

    async def get(self, id_: str, /) -> UserModel:
        stmt = select(UserTable).where(UserTable.id == id_)
        res = await self._session.execute(stmt)
        return res.fetchone()[0].to_read_model()

    async def create(self, model: UserModel, /) -> UserModel:
        stmt = (
            insert(UserTable).values(model.model_dump()).returning(UserTable)
        )
        res = await self._session.execute(stmt)
        return res.fetchone()[0].to_read_model()

    async def update(self, model: UserModel, /) -> UserModel:
        stmt = (
            update(UserTable)
            .values(model.model_dump())
            .filter_by(id=model.id)
            .returning(UserTable)
        )
        res = await self._session.execute(stmt)
        return res.fetchone()[0].to_read_model()

    async def list(
        self,
        *,
        limit: int = 100,
        offset: int = 0,
        filters: UserFilter | None = None,
    ) -> List[UserModel]:
        stmt = select(UserTable)
        if filters:
            if created_at := filters.created_at:
                stmt = self._range_filter(
                    stmt, UserTable.created_at, created_at
                )
            if updated_at := filters.updated_at:
                stmt = self._range_filter(
                    stmt, UserTable.updated_at, updated_at
                )

        stmt = stmt.limit(limit).offset(offset)
        res = await self._session.execute(stmt)
        return [row[0].to_read_model() for row in res.all()]

    async def delete(self, id_: str, /) -> None:
        stmt = delete(UserTable).where(UserTable.id == id_)
        await self._session.execute(stmt)
