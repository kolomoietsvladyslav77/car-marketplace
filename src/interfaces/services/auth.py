import abc

from gotrue.types import AuthResponse


class ISignUpSignInService(metaclass=abc.ABCMeta):
    """Interface for sign-up and sign-in functionalities."""

    @abc.abstractmethod
    async def sign_in(self, email: str, password: str) -> AuthResponse:
        """Handles user sign-in process."""

    @abc.abstractmethod
    async def sign_up(self, email: str, password: str) -> AuthResponse:
        """Handles user sign-up process."""

    @abc.abstractmethod
    async def refresh_tokens(self, token: str) -> AuthResponse:
        """Refresh tokens"""
