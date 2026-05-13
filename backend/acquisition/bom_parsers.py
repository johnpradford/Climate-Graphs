from bs4 import BeautifulSoup
import pandas as pd


class BOMClimateParser:
    def parse_climate_table(self, html: str) -> pd.DataFrame:
        soup = BeautifulSoup(html, 'html.parser')

        tables = soup.find_all('table')

        if not tables:
            raise ValueError('No climate tables found in BOM response')

        dataframe = pd.read_html(str(tables[0]))[0]

        dataframe.columns = [str(column).strip() for column in dataframe.columns]

        return dataframe
