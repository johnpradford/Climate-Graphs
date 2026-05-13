from bs4 import BeautifulSoup
import pandas as pd

from backend.acquisition.bom_schema_handler import BOMSchemaHandler


class BOMClimateParser:
    def __init__(self):
        self.schema_handler = BOMSchemaHandler()

    def parse_climate_table(self, html: str) -> pd.DataFrame:
        soup = BeautifulSoup(html, 'html.parser')

        tables = soup.find_all('table')

        if not tables:
            raise ValueError('No climate tables found in BOM response')

        selected_table = None

        for table in tables:
            try:
                dataframe = pd.read_html(str(table))[0]
                dataframe = self.schema_handler.normalise_columns(dataframe)

                self.schema_handler.validate_required_columns(dataframe)

                selected_table = dataframe
                break

            except Exception:
                continue

        if selected_table is None:
            raise ValueError('Unable to locate compatible BOM climate table')

        return selected_table
