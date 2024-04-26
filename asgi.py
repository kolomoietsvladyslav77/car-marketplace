import logging

from typing import Callable

from dependency_injector.containers import DeclarativeContainer
from fastapi import FastAPI

from containers import bootstrap


def build_app(
    bootstrap_: Callable[[str], DeclarativeContainer] = bootstrap
) -> FastAPI:
    container = bootstrap_("web")
    container.init_resources()
    logging.basicConfig(level=logging.INFO)
    app = container.fastapi_app()
    return app
