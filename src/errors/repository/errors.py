from src.errors.base_error import BaseError


class ObjectNotFound(BaseError):
    code = 400
    message = "Object not found"
    error_code = 400_01_001


class CarNotFound(ObjectNotFound):
    code = 400
    message = "Car not found"
    error_code = 400_01_002


class CarBrandNotFound(ObjectNotFound):
    code = 400
    message = "Car brand not found"
    error_code = 400_01_003


class CarSeriesNotFound(ObjectNotFound):
    code = 400
    message = "Car series not found"
    error_code = 400_01_004


class UserNotFound(ObjectNotFound):
    code = 400
    message = "User not found"
    error_code = 400_01_005
