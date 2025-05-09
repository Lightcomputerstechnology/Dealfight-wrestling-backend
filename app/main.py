from app.routers import auth, report, wallet, wrestler, match, title
from app.routers import auth, report, wallet, wrestler, match
from app.routers import auth, report, wallet, wrestler
from fastapi import FastAPI
from app.routers import auth, report, wallet

app = FastAPI(title="Dealfight Wrestling API")

app.include_router(wallet.router, prefix="/wallet", tags=["Wallet"])

@app.get("/")
def root():
    return {"message": "Welcome to Dealfight Wrestling API"}

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(report.router, prefix="/report", tags=["Reports"])

app.include_router(wrestler.router, prefix="/wrestler", tags=["Wrestler"])

app.include_router(match.router, prefix="/match", tags=["Match"])

app.include_router(title.router, prefix="/title", tags=["Title"])