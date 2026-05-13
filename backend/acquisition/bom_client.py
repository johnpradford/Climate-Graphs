from pathlib import Path
from loguru import logger
import requests


class BOMClient:
    def __init__(self, cache_dir: str = 'cache'):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def fetch(self, url: str) -> str:
        logger.info(f'Fetching BOM resource: {url}')

        response = requests.get(url, timeout=30)
        response.raise_for_status()

        return response.text
