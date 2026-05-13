from dataclasses import dataclass

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

        return await self.client.fetch(url)

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

        return {
            'station_id': request.station_id,
            'table_count': len(parsed_tables),
            'tables': [
                table.head(12).to_dict(orient='records')
                for table in parsed_tables
            ]
        }
