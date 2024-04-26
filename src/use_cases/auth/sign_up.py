from typing import Protocol

from pydantic import BaseModel

from src.errors.repository import UserNotFound
from src.errors.use_cases.auth import UserAlreadyExists
from src.interfaces.services.auth import ISignUpSignInService
from src.interfaces.services.users import IUserService
from src.models.users import UserModel


class SignUpCommand(BaseModel):
    email: str
    password: str


class SignUpUseCaseProtocol(Protocol):
    async def __call__(self, cmd: SignUpCommand, /) -> None:
        """Sign up use case"""


class SignUpUseCaseImpl:
    def __init__(
        self,
        auth_service: ISignUpSignInService,
        user_service: IUserService,
    ):
        self._auth_service = auth_service
        self._user_service = user_service

    async def __call__(self, cmd: SignUpCommand, /) -> None:
        auth_response = await self._auth_service.sign_up(
            cmd.email, cmd.password
        )

        try:
            if await self._user_service.get_by_super_id(auth_response.user.id):
                raise UserAlreadyExists()
        except UserNotFound:
            pass

        await self._user_service.create_user(
            UserModel(
                super_id=auth_response.user.id,
                email=auth_response.user.email,
            )
        )
