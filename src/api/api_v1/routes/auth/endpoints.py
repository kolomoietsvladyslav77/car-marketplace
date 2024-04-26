from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.api.api_v1.schemas.requests.auth import (
    RefreshRequestSchema,
    SignInRequestSchema,
    SignUpRequestSchema,
)
from src.api.api_v1.schemas.responses.auth import JWTTokensResponseSchema
from src.api.api_v1.schemas.responses.common import SuccessResponseSchema
from src.use_cases.auth.refresh_session import (
    RefreshSessionCommand,
    RefreshSessionUseCaseProtocol,
)
from src.use_cases.auth.sign_in import SignInCommand, SignInUseCaseProtocol
from src.use_cases.auth.sign_up import SignUpCommand, SignUpUseCaseProtocol


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    path="/sign_up/",
    response_model=SuccessResponseSchema,
)
@inject
async def sign_up(
    request: SignUpRequestSchema,
    uc: SignUpUseCaseProtocol = Depends(Provide["sign_up_use_case"]),
):
    await uc(
        SignUpCommand(
            email=request.email,
            password=request.password,
        )
    )
    return SuccessResponseSchema()


@router.post(
    path="/sign_in/",
    response_model=JWTTokensResponseSchema,
)
@inject
async def sign_in(
    request: SignInRequestSchema,
    uc: SignInUseCaseProtocol = Depends(Provide["sign_in_use_case"]),
):
    return await uc(
        SignInCommand(
            email=request.email,
            password=request.password,
        )
    )


@router.post(
    path="/refresh_tokens/",
    response_model=JWTTokensResponseSchema,
)
@inject
async def refresh_tokens(
    request: RefreshRequestSchema,
    uc: RefreshSessionUseCaseProtocol = Depends(
        Provide["refresh_session_use_case"]
    ),
):
    return await uc(
        RefreshSessionCommand(
            refresh_token=request.refresh_token,
        )
    )
