from fastapi import APIRouter

from backend.acquisition.bom_climatology_fetch import (
    BOMClimatologyFetcher,
    ClimatologyRequest,
)

router = APIRouter(
    prefix='/bom',
    tags=['bom']
)

fetcher = BOMClimatologyFetcher()


@router.get('/climatology/{station_id}')
async def climatology(
    station_id: str
):

    return await fetcher.fetch_monthly_climatology(
        ClimatologyRequest(
            station_id=station_id
        )
    )
