from dataclasses import dataclass


@dataclass
class StationCandidate:
    station_id: str
    distance_km: float
    completeness_score: float
    elevation_difference: float


class StationRanker:
    @staticmethod
    def score(candidate: StationCandidate) -> float:
        return (
            (1 / (candidate.distance_km + 1)) * 0.35
            + candidate.completeness_score * 0.30
            + (1 / (candidate.elevation_difference + 1)) * 0.15
        )
