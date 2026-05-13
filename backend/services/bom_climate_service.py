from backend.acquisition.bom_client import BOMClient
from backend.acquisition.bom_parsers import BOMClimateParser
from backend.acquisition.bom_urls import BOMUrls


class BOMClimateService:
    def __init__(self):
        self.client = BOMClient()
        self.parser = BOMClimateParser()

    def fetch_climate_statistics(self, station_id: str):
        url = BOMUrls.climate_statistics(station_id)

        html = self.client.fetch(url)

        dataframe = self.parser.parse_climate_table(html)

        return dataframe
