from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db
from app.core.permissions import admin_required
from app.models.user import User
from app.models.match import Match
from app.models.replay import Replay
from app.models.report import Report
from app.models.title import TitleBelt

router = APIRouter()

@router.get("/stats")
def get_platform_stats(db: Session = Depends(get_db), current_user: User = Depends(admin_required)):
    return {
        "users": db.query(User).count(),
        "matches": db.query(Match).count(),
        "replays": db.query(Replay).count(),
        "reports": db.query(Report).count(),
        "title_holders": db.query(TitleBelt).count()
    }
