# app/main.py
import logging
import subprocess
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, wrestler, match, replay, report, title
from app.core.database import Base, engine


# ────────────────────── Alembic migrations ──────────────────────
def run_migrations() -> None:
    """
    Upgrade DB schema to latest revision.
    If Alembic exits with a non-zero code, log the error but
    keep the API running so we can inspect logs inside Render.
    """
    try:
        subprocess.run(["alembic", "upgrade", "head"], check=True)
        logging.info("Alembic migration succeeded")
    except subprocess.CalledProcessError as exc:
        logging.error("Alembic migration failed: %s", exc)
        # Comment out the next line if you want the app to crash instead
        # raise


run_migrations()

# Optional fallback: create tables if no migrations (harmless if they exist)
Base.metadata.create_all(bind=engine)


# ───────────────────────── FastAPI app ──────────────────────────
app = FastAPI(title="Dealfight Wrestling API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to Dealfight Wrestling API"}


# ───────────────────────── Include routers ──────────────────────
app.include_router(auth.router,     prefix="/auth",      tags=["Auth"])
app.include_router(wrestler.router, prefix="/wrestlers", tags=["Wrestlers"])
app.include_router(match.router,    prefix="/matches",   tags=["Matches"])
app.include_router(replay.router,   prefix="/replays",   tags=["Replays"])
app.include_router(report.router,   prefix="/reports",   tags=["Reports"])
app.include_router(title.router,    prefix="/titles",    tags=["Titles"])