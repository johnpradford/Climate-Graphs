from io import StringIO

import pandas as pd
from bs4 import BeautifulSoup


class BOMTableParser:
    """Parse BOM climatology tables."""

    @staticmethod
    def extract_tables(html: str):

        soup = BeautifulSoup(
            html,
            'html.parser'
        )

        html_tables = soup.find_all('table')

        parsed = []

        for table in html_tables:

            try:

                parsed.extend(
                    pd.read_html(
                        StringIO(str(table))
                    )
                )

            except Exception:
                continue

        return parsed

    @staticmethod
    def normalise_month_column(df: pd.DataFrame):

        month_lookup = {
            'Jan': 1,
            'Feb': 2,
            'Mar': 3,
            'Apr': 4,
            'May': 5,
            'Jun': 6,
            'Jul': 7,
            'Aug': 8,
            'Sep': 9,
            'Oct': 10,
            'Nov': 11,
            'Dec': 12,
        }

        first_column = df.columns[0]

        normalised = df.copy()

        normalised['month'] = (
            normalised[first_column]
            .astype(str)
            .str[:3]
            .map(month_lookup)
        )

        return normalised

    @staticmethod
    def coerce_numeric_columns(df: pd.DataFrame):

        cleaned = df.copy()

        for column in cleaned.columns:

            if column == 'month':
                continue

            cleaned[column] = pd.to_numeric(
                cleaned[column],
                errors='coerce'
            )

        return cleaned
