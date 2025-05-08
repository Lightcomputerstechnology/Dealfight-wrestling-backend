# app/main.py
from fastapi import FastAPI
from app.routers import auth

app = FastAPI(title="Dealfight Wrestling API")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Dealfight Wrestling API"}