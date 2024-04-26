import datetime

from sqlalchemy import TIMESTAMP, Column, String

from src.infrastructure.tables.meta_table import MetaBase
from src.models.users import UserModel


class UserTable(MetaBase):
    __tablename__ = "users"

    id: str | Column = Column(String(36), primary_key=True)
    super_id: str | Column = Column(String(36), nullable=False)
    email: str | Column = Column(String(128), nullable=False)

    updated_at: datetime.datetime | Column = Column(
        TIMESTAMP(), nullable=False
    )
    created_at: datetime.datetime | Column = Column(
        TIMESTAMP(), nullable=False
    )

    def to_read_model(self):
        return UserModel.model_validate(self, from_attributes=True)
