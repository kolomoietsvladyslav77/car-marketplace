import datetime

from typing import List

from pydantic import BaseModel


class SeriesSchema(BaseModel):
    id: str
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class SeriesResponseSchema(BaseModel):
    id: str
    name: str
    brand_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class ListSeriesResponseSchema(BaseModel):
    series: List[SeriesResponseSchema]
