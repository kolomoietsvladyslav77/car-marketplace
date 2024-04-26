from src.models.common.models import GenericModel


class CarSeriesModel(GenericModel):
    name: str
    brand_id: str


class CarBrandModel(GenericModel):
    name: str


class CarModel(GenericModel):
    brand_id: str
    model_id: str
    year: int
    mileage: int
    user_id: str
