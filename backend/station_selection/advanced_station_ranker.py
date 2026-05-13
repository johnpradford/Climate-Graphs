from dataclasses import dataclass


@dataclass
class AdvancedStationCandidate:
    distance_score: float
    completeness_score: float
    elevation_score: float
    continuity_score: float
    climate_similarity_score: float


class AdvancedStationRanker:
    @staticmethod
    def weighted_score(candidate: AdvancedStationCandidate):
        return round(
            candidate.distance_score * 0.35
            + candidate.completeness_score * 0.30
            + candidate.elevation_score * 0.15
            + candidate.continuity_score * 0.10
            + candidate.climate_similarity_score * 0.10,
            4,
        )
