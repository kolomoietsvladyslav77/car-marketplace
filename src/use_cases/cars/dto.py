import datetime

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class ViewSeriesDTO:
    id: str
    name: str
    brand_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


@dataclass(frozen=True)
class SeriesDTO:
    id: str
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


@dataclass(frozen=True)
class ViewBrandDTO:
    id: str
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


@dataclass(frozen=True)
class ViewCarDTO:
    id: str
    brand: ViewBrandDTO
    series: SeriesDTO
    year: int
    mileage: int
    user_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


@dataclass(frozen=True)
class UpdateCarDTO:
    id: str
    brand_id: str
    series_id: str
    year: int
    mileage: int
    user_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


@dataclass(frozen=True)
class ViewCarsDTO:
    cars: List[ViewCarDTO]


@dataclass(frozen=True)
class ViewSeriesListDTO:
    series: List[ViewSeriesDTO]


@dataclass(frozen=True)
class ViewBrandsDTO:
    brands: List[ViewSeriesDTO]
