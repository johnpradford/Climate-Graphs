import requests


class BOMEndpointValidator:
    @staticmethod
    def validate(url: str) -> bool:
        response = requests.get(url, timeout=15)

        if response.status_code != 200:
            raise ValueError(f'Invalid BOM endpoint: {url}')

        if 'Bureau of Meteorology' not in response.text:
            raise ValueError('Endpoint does not appear to be a BOM climate page')

        return True
