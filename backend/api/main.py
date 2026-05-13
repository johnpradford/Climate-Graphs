from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes.bom import router as bom_router
from backend.api.routes.climate import router as climate_router
from backend.api.routes.stations import router as stations_router

app = FastAPI(
    title='Climate Summary Engine',
    version='0.1.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://localhost:5173',
    ],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(climate_router)
app.include_router(stations_router)
app.include_router(bom_router)


@app.get('/')
def healthcheck():
    return {
        'status': 'ok',
        'service': 'Climate Summary Engine API'
    }
