from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bom_extractor.infrastructure.persistence.entities import Base


def create_session_factory(database_url: str = "sqlite:///bom.db"):
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)