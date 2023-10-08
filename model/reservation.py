from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.orm import declarative_base

from utils.db import engine

Base = declarative_base()


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(String(36), primary_key=True)
    queue_number = Column(String(255), nullable=False)

    date_request = Column(DateTime(timezone=True), nullable=False)
    date_request_at = Column(DateTime(timezone=True), nullable=True)

    time_start = Column(DateTime(timezone=True), nullable=False)
    time_end = Column(DateTime(timezone=True), nullable=False)

    status = Column(String(20), nullable=False)
    reason = Column(Text, nullable=False)

    schedule_id = Column(String(26), nullable=False)
    patient_id = Column(String(26), nullable=False)
    nurse_id = Column(String(26), nullable=False)


Base.metadata.create_all(engine)
