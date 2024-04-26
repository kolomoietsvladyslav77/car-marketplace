import abc

from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from src.models.common.filters import RangeFilter


class GenericSQLAlchemyRepository(metaclass=abc.ABCMeta):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    @staticmethod
    def _range_filter(
        stmt: Any, filter_value: Any, filters: RangeFilter
    ) -> Any:
        if filters.eq:
            stmt = stmt.where(filter_value == filters.eq)
        elif any([filters.gt, filters.lt]):
            if filters.gt:
                stmt = stmt.where(filter_value > filters.gt)
            if filters.lt:
                stmt = stmt.where(filter_value < filters.lt)
        return stmt
