# app/main.py
import logging
import subprocess
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import (
    auth, wrestler, match, replay, report, title,
    wallet, notification, referral, appeal, xp,
    faq, blog, support, leaderboard, settings
)
from app.core.database import Base, engine

# ────────────────────── Alembic migrations ──────────────────────
def run_migrations() -> None:
    try:
        subprocess.run(["alembic", "upgrade", "head"], check=True)
        logging.info("Alembic migration succeeded")
    except subprocess.CalledProcessError as exc:
        logging.error("Alembic migration failed: %s", exc)

run_migrations()
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
app.include_router(auth.router,         prefix="/auth",          tags=["Auth"])
app.include_router(wrestler.router,     prefix="/wrestlers",     tags=["Wrestlers"])
app.include_router(match.router,        prefix="/matches",       tags=["Matches"])
app.include_router(replay.router,       prefix="/replays",       tags=["Replays"])
app.include_router(report.router,       prefix="/reports",       tags=["Reports"])
app.include_router(title.router,        prefix="/titles",        tags=["Titles"])
app.include_router(wallet.router,       prefix="/wallet",        tags=["Wallet"])
app.include_router(notification.router, prefix="/notifications", tags=["Notifications"])
app.include_router(referral.router,     prefix="/referrals",     tags=["Referrals"])
app.include_router(appeal.router,       prefix="/appeals",       tags=["Ban Appeals"])
app.include_router(xp.router,           prefix="/xp",            tags=["XP System"])
app.include_router(faq.router,          prefix="/faq",           tags=["FAQ"])
app.include_router(blog.router,         prefix="/blog",          tags=["Blog"])
app.include_router(support.router,      prefix="/support",       tags=["Support Chat"])
app.include_router(leaderboard.router,  prefix="/leaderboard",   tags=["Leaderboard"])
app.include_router(settings.router,     prefix="/settings",      tags=["Settings"])
