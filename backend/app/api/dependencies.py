"""API dependencies."""
from typing import Generator
from app.database.session import SessionLocal


def get_database_session() -> Generator:
    """Returns a database session."""
    try:
        database = SessionLocal()
        yield database
    finally:
        database.close()
