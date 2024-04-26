from fastapi import FastAPI

from src.api.api_v1.routes.auth import router as auth_v1_router
from src.api.api_v1.routes.cars import brand_router as brand_v1_router
from src.api.api_v1.routes.cars import car_router as car_v1_router
from src.api.api_v1.routes.cars import series_router as series_v1_router
from src.api.api_v1.routes.users import router as users_v1_router
from src.di import Lifespan
from src.errors.error_handler import EXCEPTION_HANDLERS


def create_app(
    lifespan: Lifespan,
    debug: bool = False,
) -> FastAPI:
    app = FastAPI(
        debug=debug,
        lifespan=lifespan,
        exception_handlers=EXCEPTION_HANDLERS,
    )
    app.include_router(auth_v1_router, prefix="/api/v1")
    app.include_router(users_v1_router, prefix="/api/v1")
    app.include_router(car_v1_router, prefix="/api/v1")
    app.include_router(brand_v1_router, prefix="/api/v1")
    app.include_router(series_v1_router, prefix="/api/v1")

    return app
