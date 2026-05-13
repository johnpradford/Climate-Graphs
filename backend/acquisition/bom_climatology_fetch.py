from dataclasses import dataclass
import math

from backend.acquisition.bom_client import BOMClient
from backend.acquisition.bom_table_parser import BOMTableParser
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

        serialised_tables = []

        for table in parsed_tables:

            records = table.head(12).to_dict(
                orient='records'
            )

            cleaned_records = []

            for row in records:

                cleaned_row = {}

                for key, value in row.items():
                    cleaned_row[key] = self._clean_value(value)

                cleaned_records.append(cleaned_row)

            serialised_tables.append(cleaned_records)

        return {
            'station_id': request.station_id,
            'table_count': len(parsed_tables),
            'tables': serialised_tables,
        }
