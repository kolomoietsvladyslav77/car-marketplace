from typing import Protocol

from pydantic import BaseModel

from src.interfaces.services.auth import ISignUpSignInService

from .dto import JWTTokensDTO


class SignInCommand(BaseModel):
    email: str
    password: str


class SignInUseCaseProtocol(Protocol):
    async def __call__(self, cmd: SignInCommand, /) -> JWTTokensDTO:
        """Sign in use case"""


class SignInUseCaseImpl:
    def __init__(
        self,
        auth_service: ISignUpSignInService,
    ):
        self._auth_service = auth_service

    async def __call__(self, cmd: SignInCommand, /) -> JWTTokensDTO:
        auth_response = await self._auth_service.sign_in(
            cmd.email, cmd.password
        )
        return JWTTokensDTO(
            access_token=auth_response.session.access_token,
            refresh_token=auth_response.session.refresh_token,
        )
