from dependency_injector.containers import (
    DeclarativeContainer,
    WiringConfiguration,
)
from dependency_injector.providers import Configuration, Factory, Singleton

from src.infrastructure.db import AsyncSQLAlchemy
from src.infrastructure.supabase import SupabaseClient
from src.infrastructure.unit_of_work import SQLAlchemyUnitOfWork
from src.services.auth import SignUpSignInService
from src.services.cars import CarBrandService, CarSeriesService, CarService
from src.services.users import UserService
from src.use_cases.auth.refresh_session import RefreshSessionUseCaseImpl
from src.use_cases.auth.sign_in import SignInUseCaseImpl
from src.use_cases.auth.sign_up import SignUpUseCaseImpl
from src.use_cases.cars.create_brand import CreateBrandUseCaseImpl
from src.use_cases.cars.create_car import CreateCarUseCaseImpl
from src.use_cases.cars.create_series import CreateSeriesUseCaseImpl
from src.use_cases.cars.drop_car import DropCarUseCaseImpl
from src.use_cases.cars.update_brand import UpdateBrandUseCaseImpl
from src.use_cases.cars.update_car import UpdateCarUseCaseImpl
from src.use_cases.cars.update_series import UpdateSeriesUseCaseImpl
from src.use_cases.cars.view_brands import ViewBrandUseCaseImpl
from src.use_cases.cars.view_car import ViewCarUseCaseImpl
from src.use_cases.cars.view_cars import ViewCarsUseCaseImpl
from src.use_cases.cars.view_series import ViewSeriesUseCaseImpl
from src.use_cases.users.drop_user import DropUserUseCaseImpl
from src.use_cases.users.view_user import ViewUserUseCaseImpl
from src.use_cases.users.view_users import ViewUsersUseCaseImpl


class BaseContainer(DeclarativeContainer):
    config = Configuration()

    wiring_config = WiringConfiguration(
        packages=[
            "src.api.api_v1.routes.auth",
            "src.api.api_v1.routes.cars",
            "src.api.api_v1.routes.users",
            "src.api.api_v1.routes",
        ],
    )

    # storage
    storage = Singleton(
        AsyncSQLAlchemy,
        config.db_connection_link,
    )

    # uow
    unit_of_work = Factory(
        SQLAlchemyUnitOfWork,
        storage,
    )

    # supabase client
    supabase_client = Factory(
        SupabaseClient,
        config.supabase_url,
        config.supabase_secret_key,
    )

    # services
    sign_in_sign_up_service = Factory(
        SignUpSignInService,
        supabase_client,
    )
    user_service = Factory(
        UserService,
        unit_of_work,
    )
    car_service = Factory(
        CarService,
        unit_of_work,
    )
    car_brand_service = Factory(
        CarBrandService,
        unit_of_work,
    )
    car_model_service = Factory(CarSeriesService, unit_of_work)

    # use cases
    # auth
    sign_up_use_case = Factory(
        SignUpUseCaseImpl,
        sign_in_sign_up_service,
        user_service,
    )
    sign_in_use_case = Factory(
        SignInUseCaseImpl,
        sign_in_sign_up_service,
    )
    refresh_session_use_case = Factory(
        RefreshSessionUseCaseImpl,
        sign_in_sign_up_service,
    )

    # users
    view_user_use_case = Factory(
        ViewUserUseCaseImpl,
        user_service,
    )
    view_users_use_case = Factory(
        ViewUsersUseCaseImpl,
        user_service,
    )
    drop_user_use_case = Factory(
        DropUserUseCaseImpl,
        user_service,
        car_service,
    )

    # cars
    view_car_use_case = Factory(
        ViewCarUseCaseImpl,
        car_service,
        car_brand_service,
        car_model_service,
    )
    view_cars_use_case = Factory(
        ViewCarsUseCaseImpl,
        car_service,
        car_brand_service,
        car_model_service,
    )
    update_car_use_case = Factory(
        UpdateCarUseCaseImpl,
        car_service,
        car_brand_service,
        car_model_service,
    )
    create_car_use_case = Factory(
        CreateCarUseCaseImpl,
        car_service,
        car_brand_service,
        car_model_service,
    )
    drop_car_use_case = Factory(
        DropCarUseCaseImpl,
        car_service,
    )
    view_brand_use_case = Factory(
        ViewBrandUseCaseImpl,
        car_brand_service,
    )
    update_brand_use_case = Factory(
        UpdateBrandUseCaseImpl,
        car_brand_service,
    )
    create_brand_use_case = Factory(CreateBrandUseCaseImpl, car_brand_service)
    view_series_use_case = Factory(
        ViewSeriesUseCaseImpl,
        car_model_service,
    )
    update_brand_series_use_case = Factory(
        UpdateSeriesUseCaseImpl,
        car_model_service,
        car_brand_service,
    )
    create_series_service = Factory(
        CreateSeriesUseCaseImpl,
        car_model_service,
        car_brand_service,
    )
