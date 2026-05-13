from backend.acquisition.station_metadata import MOCK_STATIONS
from backend.station_selection.spatial_search import SpatialSearch


class FallbackSelector:
    def nearest_station(self, latitude: float, longitude: float):
        ranked = []

        for station in MOCK_STATIONS:
            distance = SpatialSearch.haversine_distance(
                latitude,
                longitude,
                station.latitude,
                station.longitude,
            )

            ranked.append((distance, station))

        ranked.sort(key=lambda item: item[0])

        return ranked[0][1]
