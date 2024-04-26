from typing import List

from sqlalchemy import delete, insert, select, update

from src.errors.repository import (
    CarBrandNotFound,
    CarNotFound,
    CarSeriesNotFound,
)
from src.infrastructure.repositories.common import GenericSQLAlchemyRepository
from src.infrastructure.tables.cars import (
    CarBrandTable,
    CarSeriesTable,
    CarTable,
)
from src.models.cars import (
    CarBrandFilter,
    CarBrandModel,
    CarFilter,
    CarModel,
    CarSeriesFilter,
    CarSeriesModel,
    ICarBrandRepository,
    ICarRepository,
    ICarSeriesRepository,
)


class SQLAlchemyCarRepository(ICarRepository, GenericSQLAlchemyRepository):
    async def get(self, id_: str, /) -> CarModel:
        stmt = select(CarTable).where(CarTable.id == id_)
        res = await self._session.execute(stmt)
        if car := res.fetchone():
            return car[0].to_read_model()
        raise CarNotFound()

    async def create(self, model: CarModel, /) -> CarModel:
        stmt = insert(CarTable).values(model.model_dump()).returning(CarTable)
        res = await self._session.execute(stmt)
        return res.fetchone()[0].to_read_model()

    async def update(self, model: CarModel, /) -> CarModel:
        stmt = (
            update(CarTable)
            .values(model.model_dump())
            .filter_by(id=model.id)
            .returning(CarTable)
        )
        res = await self._session.execute(stmt)
        return res.fetchone()[0].to_read_model()

    async def list(
        self,
        *,
        limit: int = 100,
        offset: int = 0,
        filters: CarFilter | None = None,
    ) -> List[CarModel]:
        stmt = select(CarTable)
        if filters:
            if brand_names := filters.brand_names:
                stmt = stmt.join(
                    CarBrandTable,
                    CarTable.brand_id == CarBrandTable.id,
                ).where(CarBrandTable.name.in_(brand_names))
            if model_names := filters.model_names:
                stmt = (
                    stmt.join(
                        CarBrandTable, CarTable.brand_id == CarBrandTable.id
                    )
                    .join(
                        CarSeriesTable,
                        CarTable.id == CarSeriesTable.id,
                    )
                    .where(CarSeriesTable.name.in_(model_names))
                )
            if year := filters.year:
                stmt = self._range_filter(stmt, CarTable.year, year)
            if mileage := filters.mileage:
                stmt = self._range_filter(stmt, CarTable.mileage, mileage)
            if users := filters.users:
                stmt = stmt.where(CarTable.user_id.in_(users))
            if created_at := filters.created_at:
                stmt = self._range_filter(
                    stmt, CarTable.created_at, created_at
                )
            if updated_at := filters.updated_at:
                stmt = self._range_filter(
                    stmt, CarTable.updated_at, updated_at
                )

        stmt = stmt.limit(limit).offset(offset)
        res = await self._session.execute(stmt)
        return [row[0].to_read_model() for row in res.all()]

    async def delete(self, id_: str, /) -> None:
        stmt = delete(CarTable).where(CarTable.id == id_)
        await self._session.execute(stmt)

    async def delete_by_user_id(self, user_id: str) -> None:
        stmt = delete(CarTable).where(CarTable.user_id == user_id)
        await self._session.execute(stmt)


class SQLAlchemyCarBrandRepository(
    ICarBrandRepository, GenericSQLAlchemyRepository
):
    async def get(self, id_: str, /) -> CarBrandModel:
        stmt = select(CarBrandTable).where(CarBrandTable.id == id_)
        res = await self._session.execute(stmt)
        if car_brand := res.fetchone():
            return car_brand[0].to_read_model()

        raise CarBrandNotFound()

    async def create(self, model: CarBrandModel, /) -> CarBrandModel:
        stmt = (
            insert(CarBrandTable)
            .values(model.model_dump())
            .returning(CarBrandTable)
        )
        res = await self._session.execute(stmt)
        return res.fetchone()[0].to_read_model()

    async def update(self, model: CarBrandModel, /) -> CarBrandModel:
        stmt = (
            update(CarBrandTable)
            .values(model.model_dump())
            .filter_by(id=model.id)
            .returning(CarBrandTable)
        )
        res = await self._session.execute(stmt)
        return res.fetchone()[0].to_read_model()

    async def list(
        self,
        *,
        limit: int = 100,
        offset: int = 0,
        filters: CarBrandFilter | None = None,
    ) -> List[CarBrandModel]:
        stmt = select(CarBrandTable)
        if filters:
            if created_at := filters.created_at:
                stmt = self._range_filter(
                    stmt, CarBrandTable.created_at, created_at
                )
            if updated_at := filters.updated_at:
                stmt = self._range_filter(
                    stmt, CarBrandTable.updated_at, updated_at
                )

        stmt = stmt.limit(limit).offset(offset)
        res = await self._session.execute(stmt)
        return [row[0].to_read_model() for row in res.all()]

    async def delete(self, id_: str, /) -> None:
        stmt = delete(CarBrandTable).where(CarBrandTable.id == id_)
        await self._session.execute(stmt)

    async def get_by_car_id(self, car_id: str) -> CarModel:
        stmt = (
            select(CarBrandTable)
            .join(
                CarTable,
                CarBrandTable.id == CarTable.brand_id,
            )
            .where(CarTable.id == car_id)
        )
        res = await self._session.execute(stmt)
        return [row[0].to_read_model() for row in res.all()]


class SQLAlchemyCarSeriesRepository(
    ICarSeriesRepository, GenericSQLAlchemyRepository
):
    async def get(self, id_: str, /) -> CarSeriesModel:
        stmt = select(CarSeriesTable).where(CarSeriesTable.id == id_)
        res = await self._session.execute(stmt)

        if car_series := res.fetchone():
            return car_series[0].to_read_model()

        raise CarSeriesNotFound()

    async def create(self, model: CarSeriesModel, /) -> CarSeriesModel:
        stmt = (
            insert(CarSeriesTable)
            .values(model.model_dump())
            .returning(CarSeriesTable)
        )
        res = await self._session.execute(stmt)
        return res.fetchone()[0].to_read_model()

    async def update(self, model: CarSeriesModel, /) -> CarSeriesModel:
        stmt = (
            update(CarSeriesTable)
            .values(model.model_dump())
            .filter_by(id=model.id)
            .returning(CarSeriesTable)
        )
        res = await self._session.execute(stmt)
        return res.fetchone()[0].to_read_model()

    async def list(
        self,
        *,
        limit: int = 100,
        offset: int = 0,
        filters: CarSeriesFilter | None = None,
    ) -> List[CarSeriesModel]:
        stmt = select(CarSeriesTable)
        if filters:
            if created_at := filters.created_at:
                stmt = self._range_filter(
                    stmt, CarSeriesTable.created_at, created_at
                )
            if updated_at := filters.updated_at:
                stmt = self._range_filter(
                    stmt, CarSeriesTable.updated_at, updated_at
                )
            if brand_names := filters.brand_names:
                stmt = stmt.join(
                    CarBrandTable,
                    CarSeriesTable.brand_id == CarBrandTable.id,
                ).where(CarBrandTable.name.in_(brand_names))

        stmt = stmt.limit(limit).offset(offset)
        res = await self._session.execute(stmt)
        return [row[0].to_read_model() for row in res.all()]

    async def delete(self, id_: str, /) -> None:
        stmt = delete(CarSeriesTable).where(CarSeriesTable.id == id_)
        await self._session.execute(stmt)

    async def get_by_car_id(self, car_id: str) -> CarModel:
        stmt = (
            select(CarSeriesTable)
            .join(
                CarTable,
                CarSeriesTable.id == CarTable.model_id,
            )
            .where(CarTable.id == car_id)
        )
        res = await self._session.execute(stmt)
        return [row[0].to_read_model() for row in res.all()]
