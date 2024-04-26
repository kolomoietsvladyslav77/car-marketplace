import datetime

from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String

from src.infrastructure.tables.meta_table import MetaBase
from src.models.cars import CarBrandModel, CarModel, CarSeriesModel


class CarTable(MetaBase):
    __tablename__ = "cars"

    id: str | Column = Column(String(36), primary_key=True)
    brand_id: str | Column = Column(
        String(36), ForeignKey("car_brands.id"), nullable=False
    )
    model_id: str | Column = Column(
        String(36), ForeignKey("car_series.id"), nullable=False
    )
    year: str | Column = Column(Integer(), nullable=False)
    mileage: str | Column = Column(Integer(), nullable=False)
    user_id: str | Column = Column(
        String(36), ForeignKey("users.id"), nullable=False
    )

    updated_at: datetime.datetime | Column = Column(
        TIMESTAMP(), nullable=False
    )
    created_at: datetime.datetime | Column = Column(
        TIMESTAMP(), nullable=False
    )

    def to_read_model(self):
        return CarModel.model_validate(self, from_attributes=True)


class CarBrandTable(MetaBase):
    __tablename__ = "car_brands"

    id: str | Column = Column(String(36), primary_key=True)
    name: str | Column = Column(String(256), nullable=False)

    updated_at: datetime.datetime | Column = Column(
        TIMESTAMP(), nullable=False
    )
    created_at: datetime.datetime | Column = Column(
        TIMESTAMP(), nullable=False
    )

    def to_read_model(self):
        return CarBrandModel.model_validate(self, from_attributes=True)


class CarSeriesTable(MetaBase):
    __tablename__ = "car_series"

    id: str | Column = Column(String(36), primary_key=True)
    name: str | Column = Column(String(256), nullable=False)
    brand_id: str | Column = Column(
        String(36), ForeignKey("car_brands.id"), nullable=False
    )

    updated_at: datetime.datetime | Column = Column(
        TIMESTAMP(), nullable=False
    )
    created_at: datetime.datetime | Column = Column(
        TIMESTAMP(), nullable=False
    )

    def to_read_model(self):
        return CarSeriesModel.model_validate(self, from_attributes=True)
