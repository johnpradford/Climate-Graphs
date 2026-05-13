from pathlib import Path

import pandas as pd


CACHE_DIR = Path(__file__).resolve().parents[1] / 'cache'
CACHE_PATH = CACHE_DIR / 'stations.parquet'


def build_station_cache():
    """Initial placeholder BOM station cache."""

    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    stations = pd.DataFrame([
        {
            'station_id': '009021',
            'station_name': 'Perth Metro',
            'latitude': -31.9192,
            'longitude': 115.8728,
            'state': 'WA',
        },
        {
            'station_id': '004032',
            'station_name': 'Port Hedland Airport',
            'latitude': -20.3728,
            'longitude': 118.6264,
            'state': 'WA',
        },
    ])

    stations.to_parquet(CACHE_PATH, index=False)

    return CACHE_PATH


if __name__ == '__main__':
    path = build_station_cache()
    print(f'Station cache written to: {path}')
