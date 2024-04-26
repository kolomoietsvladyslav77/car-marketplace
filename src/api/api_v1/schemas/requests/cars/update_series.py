from pydantic import BaseModel, constr


class UpdateSeriesRequestSchema(BaseModel):
    id: constr(max_length=36, min_length=36) | None = None
    name: constr(max_length=255, min_length=2) | None = None
    brand_id: constr(max_length=36, min_length=36) | None = None
