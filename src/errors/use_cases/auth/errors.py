from src.errors.base_error import BaseError


class UserAlreadyExists(BaseError):
    code = 400
    message = "User already exists"
    error_code = 400_04_000
