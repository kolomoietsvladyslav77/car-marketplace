import datetime

from typing import Any, Protocol

from pydantic import BaseModel


# Range filter protocol
class RangeFilter(Protocol):
    gt: Any
    lt: Any
    eq: Any


# Range filters
class IntRangeFilter(BaseModel):
    """Filter for integer ranges"""

    gt: int | None
    lt: int | None
    eq: int | None


class DateTimeRangeFilter(BaseModel):
    """Filter for datetime ranges"""

    gt: datetime.datetime | None = None
    lt: datetime.datetime | None = None
    eq: datetime.datetime | None = None


# Generic filters
class GenericFilter(BaseModel):
    """Generic filter for all models"""

    created_at: DateTimeRangeFilter | None = None
    updated_at: DateTimeRangeFilter | None = None
