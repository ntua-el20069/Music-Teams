from sqlalchemy.orm import Session
from typing import Optional, Tuple
from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Optional, Annotated
from backend.monolith.database.database import get_db
from backend.monolith.models.models import Song, Composer, Lyricist, WroteMusic, WroteLyrics, ActiveSession, ActiveSessionModel


def get_session_by_token(db: Session, token: str) -> Optional[ActiveSessionModel]:
    found_active_session = db.query(ActiveSession).filter(ActiveSession.token == token).first()
    if not found_active_session:
        return None
    active_session_instance = ActiveSessionModel(
        token=found_active_session.token,
        username=found_active_session.username,
        role=found_active_session.role
    )
    return active_session_instance
