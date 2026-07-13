from fastapi import FastAPI
from api.route import router

app = FastAPI(
    title="Explainable Chest X-ray Triage API",
    version="1.0.0",
    description="Backend API for Low-Resource Chest X-ray Triage"
)

app.include_router(router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Explainable Chest X-ray Triage API"
    }
