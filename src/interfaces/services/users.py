import abc

from typing import List

from src.models.users import UserModel


class IUserService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def get_by_super_id(self, super_id: int) -> List[UserModel]:
        """Retrieves a user by super_id unique identifier."""

    @abc.abstractmethod
    async def get_user_by_id(self, user_id: str) -> UserModel:
        """Retrieves a user by their unique identifier."""

    @abc.abstractmethod
    async def update_user(self, user: UserModel) -> UserModel:
        """Updates the details of an existing user in the database."""

    @abc.abstractmethod
    async def create_user(self, user: UserModel) -> UserModel:
        """Creates a new user in the database."""

    @abc.abstractmethod
    async def list_users(
        self, limit: int | None = None, offset: int | None = None
    ) -> List[UserModel]:
        """Lists users from the database with optional pagination."""

    @abc.abstractmethod
    async def delete_user(self, user_id: str) -> None:
        """Drop user from the database."""
