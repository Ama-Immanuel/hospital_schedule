from sqlalchemy import Column, UUID, String, Text, DateTime
from sqlalchemy.orm import declarative_base

from utils.db import engine

class Reservation(Base):
    __tablename__ = "schedules"

    id = Column(String(36), primary_key=True)
    description = Column(Text, nullable=False)

    date_start = Column(DateTime(timezone=True), nullable=False)
    date_end = Column(DateTime(timezone=True), nullable=True)

    time_start = Column(DateTime(timezone=True), nullable=False)
    time_end = Column(DateTime(timezone=True), nullable=False)
    
    doctor_id = Column(String(26), nullable=False)
   

Base.metadata.create_all(engine)