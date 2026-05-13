from dataclasses import dataclass

import pandas as pd

from backend.acquisition.bom_client import BOMClient


@dataclass
class ObservationRequest:
    station_id: str
    survey_year: int


class BOMObservationFetcher:
    """Retrieve monthly observed climate data."""

    def __init__(self):
        self.client = BOMClient()

    async def fetch_monthly_observations(
        self,
        request: ObservationRequest
    ) -> pd.DataFrame:
        """Temporary canonical observation scaffold."""

        months = list(range(1, 13))

        return pd.DataFrame({
            'station_id': [request.station_id] * 12,
            'year': [request.survey_year] * 12,
            'month': months,
            'rainfall': [0.0] * 12,
            'tmax': [0.0] * 12,
            'tmin': [0.0] * 12,
        })
