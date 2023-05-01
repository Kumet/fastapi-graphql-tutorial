from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app.core.config import get_envs
from app.core.logger import setup_logger

logger = setup_logger(__name__)
env = get_envs()
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, echo=env.DEBUG, future=True)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = scoped_session(session_local)
    try:
        yield db
    finally:
        db.close()
