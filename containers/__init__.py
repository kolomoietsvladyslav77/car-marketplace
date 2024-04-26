from dependency_injector.containers import DeclarativeContainer

from src.settings import AppSettings

from .base import BaseContainer
from .web import WebContainer


def bootstrap(container_type: str) -> DeclarativeContainer:

    match container_type:
        case "base":
            container = BaseContainer()
        case "web":
            container = WebContainer()
        case _:
            raise Exception("Not valid container type")

    container.config.from_dict(AppSettings().model_dump())
    return container
