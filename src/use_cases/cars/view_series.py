from typing import Protocol

from pydantic import BaseModel

from src.interfaces.services.cars import ICarSeriesService

from .dto import ViewSeriesDTO, ViewSeriesListDTO


class ViewSeriesCommand(BaseModel):
    pass


class ViewSeriesUseCaseProtocol(Protocol):
    async def __call__(self, cmd: ViewSeriesCommand, /) -> ViewSeriesListDTO:
        """View series case"""


class ViewSeriesUseCaseImpl:
    def __init__(self, series_service: ICarSeriesService):
        self._series_service = series_service

    async def __call__(self, cmd: ViewSeriesCommand, /) -> ViewSeriesListDTO:
        series_list = await self._series_service.list_car_series()
        result_series = [
            ViewSeriesDTO(
                id=series.id,
                name=series.name,
                brand_id=series.brand_id,
                created_at=series.created_at,
                updated_at=series.updated_at,
            )
            for series in series_list
        ]
        return ViewSeriesListDTO(series=result_series)
