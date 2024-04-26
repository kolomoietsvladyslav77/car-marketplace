from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Security

from src.api.api_v1.schemas.requests.cars import (
    CreateBrandRequestSchema,
    CreateCarRequestSchema,
    CreateSeriesRequestSchema,
    UpdateBrandRequestSchema,
    UpdateCarRequestSchema,
    UpdateSeriesRequestSchema,
)
from src.api.api_v1.schemas.responses.cars.brand import (
    BrandResponseSchema,
    ListBrandsResponseSchema,
)
from src.api.api_v1.schemas.responses.cars.car import (
    CarResponseSchema,
    ListCarResponseSchema,
    UpdateCarResponseSchema,
)
from src.api.api_v1.schemas.responses.cars.series import (
    ListSeriesResponseSchema,
    SeriesResponseSchema,
)
from src.api.api_v1.schemas.responses.common import SuccessResponseSchema
from src.api.auth import AuthRules
from src.services.users import UserService
from src.use_cases.cars.create_brand import (
    CreateBrandCommand,
    CreateBrandUseCaseProtocol,
)
from src.use_cases.cars.create_car import (
    CreateCarCommand,
    CreateCarUseCaseProtocol,
)
from src.use_cases.cars.create_series import (
    CreateSeriesCommand,
    CreateSeriesUseCaseProtocol,
)
from src.use_cases.cars.drop_car import DropCarCommand, DropCarUseCaseProtocol
from src.use_cases.cars.update_brand import (
    UpdateBrandCommand,
    UpdateBrandUseCaseProtocol,
)
from src.use_cases.cars.update_car import (
    UpdateCarCommand,
    UpdateCarUseCaseProtocol,
)
from src.use_cases.cars.update_series import (
    UpdateSeriesCommand,
    UpdateSeriesUseCaseProtocol,
)
from src.use_cases.cars.view_brands import (
    ViewBrandCommand,
    ViewBrandUseCaseProtocol,
)
from src.use_cases.cars.view_car import ViewCarCommand, ViewCarUseCaseProtocol
from src.use_cases.cars.view_cars import (
    ViewCarsCommand,
    ViewCarsUseCaseProtocol,
)
from src.use_cases.cars.view_series import (
    ViewSeriesCommand,
    ViewSeriesUseCaseProtocol,
)

car_router = APIRouter(prefix="/cars", tags=["cars"])
brand_router = APIRouter(prefix="/brand", tags=["brand"])
series_router = APIRouter(prefix="/series", tags=["series"])


@car_router.post(
    path="/",
    response_model=CarResponseSchema,
)
@inject
async def create_car(
    request: CreateCarRequestSchema,
    super_user_id: str = Security(AuthRules),
    user_service: UserService = Depends(Provide["user_service"]),
    uc: CreateCarUseCaseProtocol = Depends(Provide["create_car_use_case"]),
):
    user = await user_service.get_by_super_id(super_user_id)
    return await uc(
        CreateCarCommand(**(request.model_dump() | dict(user_id=user.id)))
    )


@car_router.put(
    path="/{car_id}/",
    response_model=UpdateCarResponseSchema,
)
@inject
async def update_car(
    car_id: str,
    request: UpdateCarRequestSchema,
    super_user_id: str = Security(AuthRules),
    uc: UpdateCarUseCaseProtocol = Depends(Provide["update_car_use_case"]),
):
    return await uc(
        UpdateCarCommand(**(request.model_dump() | dict(id=car_id)))
    )


@car_router.get(
    path="/",
    response_model=ListCarResponseSchema,
)
@inject
async def view_cars(
    super_user_id: str = Security(AuthRules),
    uc: ViewCarsUseCaseProtocol = Depends(Provide["view_cars_use_case"]),
):
    return await uc(ViewCarsCommand())


@car_router.get(
    path="/{car_id}/",
    response_model=CarResponseSchema,
)
@inject
async def view_car(
    car_id: str,
    super_user_id: str = Security(AuthRules),
    uc: ViewCarUseCaseProtocol = Depends(Provide["view_car_use_case"]),
):
    return await uc(ViewCarCommand(car_id=car_id))


@car_router.delete(
    path="/{car_id}/",
    response_model=SuccessResponseSchema,
)
@inject
async def drop_car(
    car_id: str,
    super_user_id: str = Security(AuthRules),
    uc: DropCarUseCaseProtocol = Depends(Provide["drop_car_use_case"]),
):
    return await uc(DropCarCommand(car_id=car_id))


@brand_router.post(
    path="/",
    response_model=BrandResponseSchema,
)
@inject
async def create_brand(
    request: CreateBrandRequestSchema,
    super_user_id: str = Security(AuthRules),
    uc: CreateBrandUseCaseProtocol = Depends(Provide["create_brand_use_case"]),
):
    return await uc(CreateBrandCommand(**request.model_dump()))


@brand_router.put(
    path="/{brand_id}/",
    response_model=BrandResponseSchema,
)
@inject
async def update_brand(
    brand_id: str,
    request: UpdateBrandRequestSchema,
    super_user_id: str = Security(AuthRules),
    uc: UpdateBrandUseCaseProtocol = Depends(Provide["update_brand_use_case"]),
):
    return await uc(
        UpdateBrandCommand(**(request.model_dump() | dict(id=brand_id)))
    )


@brand_router.get(
    path="/",
    response_model=ListBrandsResponseSchema,
)
@inject
async def view_brands(
    super_user_id: str = Security(AuthRules),
    uc: ViewBrandUseCaseProtocol = Depends(Provide["view_brand_use_case"]),
):
    return await uc(ViewBrandCommand())


@series_router.post(
    path="/",
    response_model=SeriesResponseSchema,
)
@inject
async def create_series(
    request: CreateSeriesRequestSchema,
    super_user_id: str = Security(AuthRules),
    uc: CreateSeriesUseCaseProtocol = Depends(
        Provide["create_series_service"]
    ),
):
    return await uc(CreateSeriesCommand(**request.model_dump()))


@series_router.put(
    path="/{series_id}/",
    response_model=SeriesResponseSchema,
)
@inject
async def update_series(
    series_id: str,
    request: UpdateSeriesRequestSchema,
    super_user_id: str = Security(AuthRules),
    uc: UpdateSeriesUseCaseProtocol = Depends(
        Provide["update_brand_series_use_case"]
    ),
):
    return await uc(
        UpdateSeriesCommand(**(request.model_dump() | dict(id=series_id)))
    )


@series_router.get(
    path="/",
    response_model=ListSeriesResponseSchema,
)
@inject
async def view_series(
    super_user_id: str = Security(AuthRules),
    uc: ViewSeriesUseCaseProtocol = Depends(Provide["view_series_use_case"]),
):
    return await uc(ViewSeriesCommand())
