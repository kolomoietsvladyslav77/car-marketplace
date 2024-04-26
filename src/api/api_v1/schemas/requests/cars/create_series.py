from pydantic import BaseModel, Field


class CreateSeriesRequestSchema(BaseModel):
    name: str = Field(max_length=36)
    brand_id: str = Field(max_length=36, min_length=36)
