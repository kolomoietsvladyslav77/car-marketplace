import abc
import datetime

from pydantic import BaseModel, Field

from src.models.utils import uuid_generator


class GenericModel(BaseModel, abc.ABC):
    id: str = Field(default_factory=uuid_generator)
    created_at: datetime.datetime = Field(
        default_factory=datetime.datetime.utcnow
    )
    updated_at: datetime.datetime = Field(
        default_factory=datetime.datetime.utcnow
    )
