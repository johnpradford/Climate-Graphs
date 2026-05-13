from backend.acquisition.bom_climatology_fetch import (
    BOMClimatologyFetcher,
    ClimatologyRequest,
)
from backend.acquisition.bom_observation_fetch import (
    BOMObservationFetcher,
    ObservationRequest,
)
from backend.anomalies.rainfall import RainfallAnomalyCalculator
from backend.transformations.month_rotation import rotate_months
from backend.validation.climate_validation import ClimateValidator


class ClimatePipelineService:
    """Central orchestration layer for climate processing."""

    def __init__(self):
        self.climatology_fetcher = BOMClimatologyFetcher()
        self.observation_fetcher = BOMObservationFetcher()

    async def build_pipeline(
        self,
        station_id: str,
        survey_year: int,
        survey_month: int,
    ):

        climatology = (
            await self.climatology_fetcher.fetch_monthly_climatology(
                ClimatologyRequest(station_id=station_id)
            )
        )

        observations = (
            await self.observation_fetcher.fetch_monthly_observations(
                ObservationRequest(
                    station_id=station_id,
                    survey_year=survey_year,
                )
            )
        )

        ClimateValidator.validate_month_completeness(
            observations.rename(columns={'rainfall': 'value'})
        )

        rotated = rotate_months(
            observations,
            survey_month=survey_month,
        )

        rolling_3m = RainfallAnomalyCalculator.rolling_total(
            rotated.rename(columns={'rainfall': 'value'}),
            window=3,
        )

        return {
            'station_id': station_id,
            'survey_year': survey_year,
            'survey_month': survey_month,
            'observations': observations.to_dict(orient='records'),
            'climatology': climatology.to_dict(orient='records'),
            'rolling_3m': rolling_3m.fillna(0).tolist(),
        }
