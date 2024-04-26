import abc


class BaseError(Exception, metaclass=abc.ABCMeta):
    code = 400
    message = "Base error"
    error_code = 400_00_000
