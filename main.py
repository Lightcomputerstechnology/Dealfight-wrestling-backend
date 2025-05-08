
# app/main.py
from app.routers import result
from app.routers import title
from app.routers import match
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

app.include_router(match.router, prefix="/matches", tags=["Matches"])

app.include_router(title.router, prefix="/titles", tags=["Titles"])

app.include_router(result.router, prefix="/result", tags=["Results"])


