from src.errors.base_error import BaseError


class UnsupportedSeriesForCar(BaseError):
    code = 400
    message = "Unsupported series for car"
    error_code = 400_03_001
