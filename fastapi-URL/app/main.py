from fastapi import FastAPI
from app.routes.endpoints import router

# initialize FastAPI app and include all API routes under "/api"
app = FastAPI(title="FastAPI URL shortener", version="1.0.0")  

app.include_router(router, prefix="/api")