from pydantic import BaseModel, Field


class CreateCarRequestSchema(BaseModel):
    brand_id: str = Field(min_length=36, max_length=36)
    model_id: str = Field(min_length=36, max_length=36)
    year: int = Field(ge=1900)
    mileage: int = Field(ge=0)
