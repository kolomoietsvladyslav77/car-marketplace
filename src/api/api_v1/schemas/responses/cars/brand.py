import datetime

from typing import List

from pydantic import BaseModel


class BrandResponseSchema(BaseModel):
    id: str
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class ListBrandsResponseSchema(BaseModel):
    brands: List[BrandResponseSchema]
