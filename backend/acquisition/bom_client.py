from pathlib import Path

from loguru import logger
import requests


class BOMClient:
    HEADERS = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/124.0 Safari/537.36'
        ),
        'Accept': (
            'text/html,application/xhtml+xml,'
            'application/xml;q=0.9,*/*;q=0.8'
        ),
        'Accept-Language': 'en-AU,en;q=0.9',
        'Connection': 'keep-alive',
    }

    def __init__(self, cache_dir: str = 'cache'):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def fetch(self, url: str) -> str:
        logger.info(f'Fetching BOM resource: {url}')

        response = requests.get(
            url,
            headers=self.HEADERS,
            timeout=30,
        )

        response.raise_for_status()

        return response.text
