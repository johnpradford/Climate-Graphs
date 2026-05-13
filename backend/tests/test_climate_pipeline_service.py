import pytest

from backend.services.climate_pipeline_service import (
    ClimatePipelineService,
)


@pytest.mark.asyncio
async def test_pipeline_builds():

    service = ClimatePipelineService()

    result = await service.build_pipeline(
        station_id='009021',
        survey_year=2025,
        survey_month=10,
    )

    assert result['station_id'] == '009021'
    assert len(result['observations']) == 12
