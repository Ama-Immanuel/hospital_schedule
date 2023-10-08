from sqlalchemy import Column, UUID, String, Text
from sqlalchemy.orm import declarative_base

from utils.db import engine

Base = declarative_base()


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    phone_number = Column(String(16))
    code = Column(String(10), unique=True)
    password = Column(Text, nullable=False)


Base.metadata.create_all(engine)
