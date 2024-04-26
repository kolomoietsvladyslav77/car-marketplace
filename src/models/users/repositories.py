import abc

from src.models.common.repositories import GenericRepository

from .filters import UserFilter
from .models import UserModel


class IUserRepository(
    GenericRepository[UserModel, UserFilter], metaclass=abc.ABCMeta
):
    """Repository for UserModel entity"""

    @abc.abstractmethod
    async def get_by_super_id(self, id_: int, /) -> UserModel:
        """Get user by super_id"""
