
# app/main.py
from app.routers import wallet
from app.routers import wrestler
from fastapi import FastAPI
from app.routers import auth

app = FastAPI(title="Dealfight Wrestling API")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Dealfight Wrestling API"}
app.include_router(wrestler.router, prefix="/wrestlers", tags=["Wrestlers"])

app.include_router(wallet.router, prefix="/wallet", tags=["Wallet"])