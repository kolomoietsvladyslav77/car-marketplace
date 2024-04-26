from typing import List

from src.interfaces import IUnitOfWork
from src.interfaces.services.users import IUserService
from src.models.users import UserModel


class UserService(IUserService):
    def __init__(self, unit_of_work: IUnitOfWork):
        self._unit_of_work = unit_of_work

    async def get_by_super_id(self, super_id: int) -> UserModel:
        async with self._unit_of_work as uow:
            return await uow.users.get_by_super_id(super_id)

    async def get_user_by_id(self, user_id: str) -> UserModel:
        async with self._unit_of_work as uow:
            return await uow.users.get(user_id)

    async def update_user(self, user: UserModel) -> UserModel:
        async with self._unit_of_work as uow:
            user = await uow.users.update(user)
            await uow.commit()
            return user

    async def create_user(self, user: UserModel) -> UserModel:
        async with self._unit_of_work as uow:
            user = await uow.users.create(user)
            await uow.commit()
            return user

    async def list_users(
        self, limit: int | None = None, offset: int | None = None
    ) -> List[UserModel]:
        request_kwargs = dict()
        if limit is not None:
            request_kwargs["limit"] = limit
        if offset is not None:
            request_kwargs["offset"] = offset

        async with self._unit_of_work as uow:
            return await uow.users.list(**request_kwargs)

    async def delete_user(self, user_id: str) -> None:
        async with self._unit_of_work as uow:
            await uow.users.delete(user_id)
            await uow.commit()
