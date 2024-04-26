from pydantic import BaseModel, Field


class CreateBrandRequestSchema(BaseModel):
    name: str = Field(min_length=2, max_length=36)
