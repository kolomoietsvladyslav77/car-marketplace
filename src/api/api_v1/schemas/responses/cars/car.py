import datetime

from typing import List

from pydantic import BaseModel

from .brand import BrandResponseSchema
from .series import SeriesSchema


class CarResponseSchema(BaseModel):
    id: str
    brand: BrandResponseSchema
    series: SeriesSchema
    year: int
    mileage: int
    user_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UpdateCarResponseSchema(BaseModel):
    id: str
    brand_id: str
    series_id: str
    year: int
    mileage: int
    user_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class ListCarResponseSchema(BaseModel):
    cars: List[CarResponseSchema]
