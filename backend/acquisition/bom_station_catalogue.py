from pathlib import Path

import pandas as pd


CACHE_PATH = (
    Path(__file__).resolve().parents[1]
    / 'cache/stations.parquet'
)


class BOMStationCatalogue:
    """Load and query cached BOM station metadata."""

    def __init__(self):
        self.df = self._load()

    def _load(self) -> pd.DataFrame:

        if not CACHE_PATH.exists():
            return pd.DataFrame(
                columns=[
                    'station_id',
                    'station_name',
                    'latitude',
                    'longitude',
                    'state',
                ]
            )

        return pd.read_parquet(CACHE_PATH)

    def search(self, query: str, limit: int = 10):

        matches = self.df[
            self.df['station_name']
            .str.contains(query, case=False, na=False)
        ]

        return matches.head(limit).to_dict(orient='records')
