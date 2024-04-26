from typing import List

from src.models.common.filters import GenericFilter, IntRangeFilter


class CarFilter(GenericFilter):
    """Filter class for Car"""

    model_names: List[str] | None = None
    brand_names: List[str] | None = None
    year: IntRangeFilter | None = None
    mileage: IntRangeFilter | None = None
    users: List[str] | None = None


class CarBrandFilter(GenericFilter):
    """Filter class for CarBrand"""


class CarSeriesFilter(GenericFilter):
    """Filter class for CarSeries"""

    brand_names: List[str] | None = None
