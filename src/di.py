from typing import Any

from dependency_injector.containers import Container
from typing_extensions import Self


class Lifespan:
    def __init__(self, container: Container) -> None:
        self.container = container

    async def __aenter__(self) -> None:
        result = self.container.init_resources()

        if result is not None:
            await result

    async def __aexit__(self, *exc_info: Any) -> None:
        result = self.container.shutdown_resources()

        if result is not None:
            await result

    def __call__(self, *args: Any, **kwargs: Any) -> Self:
        return self
