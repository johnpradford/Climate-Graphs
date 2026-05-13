from dataclasses import dataclass


@dataclass
class ClimateMetric:
    name: str
    survey_value: float
    long_term_average: float

    @property
    def anomaly(self) -> float:
        return round(self.survey_value - self.long_term_average, 2)
