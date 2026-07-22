from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    database_url: str = ""
    debug: bool = False

    # model_config = {"env_file": ".env"}


settings = Settings()
engine = create_engine(settings.database_url, echo=settings.debug)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
  pass

def get_db():
  db: Session = SessionLocal()
  try:
    yield db
  finally:
    db.close()
