from fastapi import FastAPI

app = FastAPI(
    title='Climate Summary Engine',
    version='0.1.0'
)


@app.get('/')
def healthcheck():
    return {
        'status': 'ok',
        'service': 'Climate Summary Engine API'
    }
