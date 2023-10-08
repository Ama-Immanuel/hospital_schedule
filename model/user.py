from sqlalchemy import Column, UUID, String, Text
from sqlalchemy.orm import declarative_base

from utils.db import engine

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    phone_number = Column(String(16), nullable=False)
    password = Column(Text, nullable=False)
    email = Column(String(255), nullable=True)
    code = Column(String(10), unique=True, nullable=True)
    role = Column(String(10), nullable=False)

Base.metadata.create_all(engine)
