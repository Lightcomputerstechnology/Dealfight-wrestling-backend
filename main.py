from routers import admin
from routers import report
from routers import replay
from routers import result
from routers import title
from routers import match
from routers import wallet
from routers import wrestler
from routers import auth
from fastapi import FastAPI

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
app.include_router(replay.router, prefix="/replays", tags=["Replay"])
app.include_router(report.router, prefix="/report", tags=["Reports"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])