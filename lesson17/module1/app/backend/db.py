from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.util.preloaded import engine_url
from  sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///taskmanager.db', echo=True)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

# class User(Base):
#     __tablename__ = "user"
#
#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     password = Column(String)
