from fastapi import Request
from fastapi.responses import JSONResponse

from src.errors.base_error import BaseError


async def base_exception_handler(_: Request, exc: BaseError) -> JSONResponse:
    return JSONResponse(
        {
            "detail": exc.message,
            "error_code": exc.error_code,
        },
        status_code=exc.code,
    )


EXCEPTION_HANDLERS = {
    BaseError: base_exception_handler,
}
