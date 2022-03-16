import uvicorn as uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app import routers
from app.config import config

app = FastAPI()
app.include_router(routers.auth_router)
app.include_router(routers.patients_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == "__main__":
    uvicorn.run(app, host=config.host, port=config.port)
