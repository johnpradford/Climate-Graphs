from pathlib import Path
import json


class CacheManager:
    def __init__(self, cache_dir: str = 'cache'):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def write_json(self, key: str, payload: dict):
        path = self.cache_dir / f'{key}.json'

        with open(path, 'w', encoding='utf-8') as file:
            json.dump(payload, file, indent=2)

    def read_json(self, key: str):
        path = self.cache_dir / f'{key}.json'

        if not path.exists():
            return None

        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
