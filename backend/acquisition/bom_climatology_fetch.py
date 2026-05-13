from dataclasses import dataclass
import math

import pandas as pd

from backend.acquisition.bom_client import BOMClient
from backend.acquisition.bom_table_parser import BOMTableParser
from backend.acquisition.bom_url_builder import BOMUrlBuilder
from backend.anomalies.rainfall_anomaly import (
    RainfallAnomalyCalculator,
)
from backend.transformations.climatology_transformer import (
    ClimatologyTransformer,
)
from backend.validation.climatology_validator import (
    ClimatologyValidator,
)


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

        url = BOMUrlBuilder.monthly_climatology_url(
            station_id
        )

        return self.client.fetch(url)

    @staticmethod
    def _clean_value(value):

        if isinstance(value, float):

            if math.isnan(value):
                return None

        return value

    async def fetch_monthly_climatology(
        self,
        request: ClimatologyRequest
    ) -> dict:

        html = await self.fetch_raw_html(
            request.station_id
        )

        tables = BOMTableParser.extract_tables(
            html
        )

        parsed_tables = []

        for table in tables:

            try:

                normalised = (
                    BOMTableParser
                    .normalise_month_column(table)
                )

                cleaned = (
                    BOMTableParser
                    .coerce_numeric_columns(normalised)
                )

                parsed_tables.append(cleaned)

            except Exception:
                continue

        canonical_data = []
        validation_results = {}
        anomaly_data = []

        if parsed_tables:

            canonical_table = (
                ClimatologyTransformer
                .extract_canonical_monthly_data(
                    parsed_tables[0]
                )
            )

            validation_results = (
                ClimatologyValidator
                .validate(canonical_table)
            )

            anomaly_table = (
                RainfallAnomalyCalculator
                .rolling_rainfall(canonical_table)
            )

            records = anomaly_table.to_dict(
                orient='records'
            )

            for row in records:

                cleaned_row = {}

                for key, value in row.items():
                    cleaned_row[key] = self._clean_value(value)

                canonical_data.append(cleaned_row)

            anomaly_data = canonical_data

        return {
            'station_id': request.station_id,
            'table_count': len(parsed_tables),
            'validation': validation_results,
            'canonical_monthly_climatology': canonical_data,
            'rainfall_anomalies': anomaly_data,
        }
