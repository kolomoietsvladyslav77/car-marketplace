from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Path, Security

from src.api.api_v1.schemas.responses.users import (
    ListUsersResponseSchema,
    UsersResponseSchema,
)
from src.api.auth import AuthRules
from src.use_cases.users.view_user import (
    ViewUserCommand,
    ViewUserUseCaseProtocol,
)
from src.use_cases.users.view_users import ViewUsersCommand


router = APIRouter(prefix="/users", tags=["users"])


@router.get(
    path="/{user_id}/",
    response_model=UsersResponseSchema,
)
@inject
async def get_by_id(
    user_id: str = Path(..., description="The ID of the user to retrieve"),
    access_token: str = Security(AuthRules),
    uc: ViewUserUseCaseProtocol = Depends(Provide["view_user_use_case"]),
):
    return await uc(
        ViewUserCommand(
            user_id=user_id,
        )
    )


@router.get(
    path="/",
    response_model=ListUsersResponseSchema,
)
@inject
async def get_users(
    access_token: str = Security(AuthRules),
    uc: ViewUserUseCaseProtocol = Depends(Provide["view_users_use_case"]),
):
    return await uc(ViewUsersCommand())
