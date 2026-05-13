from dataclasses import dataclass

import pandas as pd

from backend.acquisition.bom_client import BOMClient
from backend.acquisition.bom_url_builder import BOMUrlBuilder


@dataclass
class ClimatologyRequest:
    station_id: str
    baseline_start: int = 1991
    baseline_end: int = 2020


class BOMClimatologyFetcher:
    """Retrieve and normalise BOM climatology datasets."""

    def __init__(self):
        self.client = BOMClient()

    async def fetch_raw_html(
        self,
        station_id: str,
    ) -> str:
        """Retrieve raw BOM climatology HTML."""

        url = BOMUrlBuilder.monthly_climatology_url(
            station_id
        )

        return await self.client.fetch(url)

    async def fetch_monthly_climatology(
        self,
        request: ClimatologyRequest
    ) -> pd.DataFrame:
        """
        Retrieve BOM climatology and return
        canonical dataframe structure.
        """

        html = await self.fetch_raw_html(
            request.station_id
        )

        months = list(range(1, 13))

        return pd.DataFrame({
            'station_id': [request.station_id] * 12,
            'month': months,
            'rainfall_climatology': [0.0] * 12,
            'tmax_climatology': [0.0] * 12,
            'tmin_climatology': [0.0] * 12,
            'baseline_start': [request.baseline_start] * 12,
            'baseline_end': [request.baseline_end] * 12,
            'html_length': [len(html)] * 12,
        })
