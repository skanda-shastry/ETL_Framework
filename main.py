from fastapi import FastAPI
from app.routes.routes import router as etl_router

app = FastAPI(title="ETL API Framework")

# Include Routes
app.include_router(etl_router, prefix="/api/v1", tags=["ETL"])

@app.get("/")
async def root():
    return {"message": "Welcome to the ETL Framework!"}
