from typing import Generator

from sqlalchemy.orm import Session

from app.db.session import SessionLocal

def get_db() -> Generator[Session, None, None]:
    """
    Dependency function that yields db sessions
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 