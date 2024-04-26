from dependency_injector.containers import WiringConfiguration
from dependency_injector.providers import Factory, Self, Singleton

from containers.base import BaseContainer
from factories.app import create_app
from src.di import Lifespan


class WebContainer(BaseContainer):
    wiring_config = WiringConfiguration(
        packages=[
            "src.api.api_v1.routes.auth",
            "src.api.api_v1.routes.cars",
            "src.api.api_v1.routes.users",
            "src.api.api_v1.routes",
        ],
    )

    __self__ = Self()
    lifespan = Singleton(Lifespan, __self__)

    fastapi_app = Factory(
        create_app,
        lifespan,
        BaseContainer.config.debug,
    )
