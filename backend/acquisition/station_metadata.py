from dataclasses import dataclass


@dataclass
class StationMetadata:
    station_id: str
    name: str
    latitude: float
    longitude: float
    elevation_m: float


MOCK_STATIONS = [
    StationMetadata('009021', 'Perth Metro', -31.9505, 115.8605, 15),
    StationMetadata('004032', 'Karratha Aero', -20.7122, 116.7738, 9),
    StationMetadata('012038', 'Albany Airport', -34.9439, 117.8089, 69),
]


def get_station_metadata(name: str):
    for station in MOCK_STATIONS:
        if station.name.lower() == name.lower():
            return station

    return None
