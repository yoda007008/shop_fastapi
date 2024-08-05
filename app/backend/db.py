from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("postgresql+psycopg2://youuser:youpassword@localhost/youdb", echo=True)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass


