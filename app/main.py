import subprocess
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, wrestler, match, replay, report, title
from app.core.database import Base, engine

# Auto-run Alembic migrations
subprocess.run(["alembic", "upgrade", "head"], check=True)

# Optional: Create tables if no migrations (usually not needed if using Alembic)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Dealfight Wrestling API")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Dealfight Wrestling API"}

# Include routers
app.include_router(auth.router,     prefix="/auth",      tags=["Auth"])
app.include_router(wrestler.router, prefix="/wrestlers", tags=["Wrestlers"])
app.include_router(match.router,    prefix="/matches",   tags=["Matches"])
app.include_router(replay.router,   prefix="/replays",   tags=["Replays"])
app.include_router(report.router,   prefix="/reports",   tags=["Reports"])
app.include_router(title.router,    prefix="/titles",    tags=["Titles"])