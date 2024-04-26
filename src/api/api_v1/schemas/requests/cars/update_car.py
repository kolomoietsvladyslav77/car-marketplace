from pydantic import BaseModel, conint, constr


class UpdateCarRequestSchema(BaseModel):
    brand_id: constr(min_length=36, max_length=36) | None = None
    model_id: constr(min_length=36, max_length=36) | None = None
    year: conint(ge=1900) | None = None
    mileage: conint(ge=0) | None = None
