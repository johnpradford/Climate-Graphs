from fastapi import FastAPI

from backend.api.routes.climate import router as climate_router

app = FastAPI(
    title='Climate Summary Engine',
    version='0.1.0'
)

app.include_router(climate_router)


@app.get('/')
def healthcheck():
    return {
        'status': 'ok',
        'service': 'Climate Summary Engine API'
    }
