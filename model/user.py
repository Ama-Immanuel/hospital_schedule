from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import declarative_base, relationship

from utils.db import engine

Base = declarative_base()

ROLE_PATIENT = "patient"
ROLE_DOCTOR = "doctor"
ROLE_NURSE = "nurse"
ROLE_ADMIN = "admin"


class UserTable(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    phone_number = Column(String(16), nullable=False)
    password = Column(Text, nullable=False)
    email = Column(String(255), nullable=False)
    code = Column(String(10), unique=True, nullable=True)
    role = Column(String(10), nullable=False, default=ROLE_PATIENT)
    # schedules = relationship("ScheduleTable", back_populates="doctors")


class User(BaseModel):
    id: str
    name: str
    phone_number: str
    email: str
    code: Optional[str]
    role: str

    @staticmethod
    def from_model_table(user_table: UserTable):
        return User(id=user_table.id,
                    email=user_table.email,
                    name=user_table.name,
                    phone_number=user_table.phone_number,
                    code=user_table.code,
                    role=user_table.role)


Base.metadata.create_all(engine)
