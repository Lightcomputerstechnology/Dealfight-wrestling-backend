from app.main import app
import subprocess
from fastapi import FastAPI

from app.routers import (
    auth,
    report,
    wallet,
    wrestler,
    match,
    title,
    replay,
    admin,
)

app = FastAPI(title="Dealfight Wrestling API")

@app.get("/")
def root():
    return {"message": "Welcome to Dealfight Wrestling API"}

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(report.router, prefix="/report", tags=["Reports"])
app.include_router(wallet.router, prefix="/wallet", tags=["Wallet"])
app.include_router(wrestler.router, prefix="/wrestler", tags=["Wrestler"])
app.include_router(match.router, prefix="/match", tags=["Match"])
app.include_router(title.router, prefix="/title", tags=["Title"])
app.include_router(replay.router, prefix="/replay", tags=["Replay"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])

# Run Alembic migration automatically at startup
try:
    subprocess.run(["alembic", "upgrade", "head"], check=True)
except Exception as e:
    print("Alembic migration failed:", e)