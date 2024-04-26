from pydantic import BaseModel


class UpdateBrandRequestSchema(BaseModel):
    id: str | None = None
    name: str | None = None
