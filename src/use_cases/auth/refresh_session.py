from typing import Protocol

from pydantic import BaseModel

from src.interfaces.services.auth import ISignUpSignInService

from .dto import JWTTokensDTO


class RefreshSessionCommand(BaseModel):
    token: str


class RefreshSessionUseCaseProtocol(Protocol):
    async def __call__(self, cmd: RefreshSessionCommand, /) -> JWTTokensDTO:
        """Refresh session use case"""


class RefreshSessionUseCaseImpl:
    def __init__(
        self,
        auth_service: ISignUpSignInService,
    ):
        self._auth_service = auth_service

    async def __call__(self, cmd: RefreshSessionCommand, /) -> JWTTokensDTO:
        auth_response = await self._auth_service.refresh_tokens(cmd.token)
        return JWTTokensDTO(
            access_token=auth_response.session.access_token,
            refresh_token=auth_response.session.refresh_token,
        )
