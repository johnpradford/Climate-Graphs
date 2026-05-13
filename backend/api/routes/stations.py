from fastapi import APIRouter

from backend.acquisition.bom_station_catalogue import (
    BOMStationCatalogue,
)


router = APIRouter(prefix='/stations', tags=['stations'])

catalogue = BOMStationCatalogue()


@router.get('/search')
def search_stations(query: str):
    """Search cached BOM station metadata."""

    return catalogue.search(query)
