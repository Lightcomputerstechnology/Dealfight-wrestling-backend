from fastapi import FastAPI
from app.routers import auth, report, wallet
app = FastAPI(title="Dealfight Wrestling API")

@app.get("/")
def root():
    return {"message": "Welcome to Dealfight Wrestling API"}

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(report.router, prefix="/report", tags=["Reports"])