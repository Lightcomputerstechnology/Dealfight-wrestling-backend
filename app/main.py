import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from app.routers import user_setting


# Import routers
from app.routers import (
    auth, wrestler, match, replay, report, title,
    wallet, notification, referral, appeal, xp,
    faq, blog, support, leaderboard, settings,
    admin_stats
)

from app.middleware.rate_limiter import RateLimiterMiddleware
from app.middleware.pagination import PaginationMiddleware
from app.core.database import Base, engine

# ─────────────────────── Create Tables Directly ───────────────────────
Base.metadata.create_all(bind=engine)

# ─────────────────────────── FastAPI App ──────────────────────────────
app = FastAPI(title="Dealfight Wrestling API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_setting.router)
app.add_middleware(RateLimiterMiddleware)
app.add_middleware(PaginationMiddleware)

@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    return JSONResponse(status_code=404, content={"error": "Route not found"})

@app.get("/")
def read_root():
    return {"message": "Welcome to Dealfight Wrestling API"}

# ─────────────────────────── Include Routers ──────────────────────────
app.include_router(auth.router,         prefix="/auth",          tags=["Auth"])
app.include_router(wrestler.router,     prefix="/wrestlers",     tags=["Wrestlers"])
app.include_router(match.router,        prefix="/matches",       tags=["Matches"])
app.include_router(replay.router,       prefix="/replays",       tags=["Replays"])
app.include_router(report.router,       prefix="/reports",       tags=["Reports"])
app.include_router(title.router,        prefix="/titles",        tags=["Titles"])
app.include_router(wallet.router,       prefix="/wallet",        tags=["Wallet"])
app.include_router(notification.router, prefix="/notifications", tags=["Notifications"])
app.include_router(referral.router,     prefix="/referrals",     tags=["Referrals"])
app.include_router(appeal.router,       prefix="/appeals",       tags=["Appeals"])
app.include_router(xp.router,           prefix="/xp",            tags=["XP System"])
app.include_router(faq.router,          prefix="/faq",           tags=["FAQ"])
app.include_router(blog.router,         prefix="/blog",          tags=["Blog"])
app.include_router(support.router,      prefix="/support",       tags=["Support Chat"])
app.include_router(leaderboard.router,  prefix="/leaderboard",   tags=["Leaderboard"])
app.include_router(settings.router,     prefix="/settings",      tags=["Settings"])
app.include_router(admin_stats.router,  prefix="/admin",         tags=["Admin Stats"])
