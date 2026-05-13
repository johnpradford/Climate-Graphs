from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.climate_summary_service import ClimateSummaryService
from backend.transformations.month_rotation import rotate_months

router = APIRouter(prefix='/climate', tags=['climate'])


class ClimateRequest(BaseModel):
    station: str
    survey_month: str
    survey_year: int


@router.post('/summary')
def generate_summary(request: ClimateRequest):
    rotated_months = rotate_months(request.survey_month[:3])

    service = ClimateSummaryService()

    summary = service.generate(
        station=request.station,
        survey_year=request.survey_year,
    )

    return {
        'station': request.station,
        'survey_year': request.survey_year,
        'rotated_months': rotated_months,
        'summary': summary,
        'status': 'complete'
    }
