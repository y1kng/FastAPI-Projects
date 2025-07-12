from fastapi import FastAPI
from app.routes import router

app = FastAPI()

app.include_router(router)      # not .include_routes, is .include_router