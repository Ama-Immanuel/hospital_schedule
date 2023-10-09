from sqlalchemy import Column, UUID, String, Text, DateTime
from sqlalchemy.orm import declarative_base, relationship
from typing import List

from utils.db import engine

Base = declarative_base()


class ScheduleTable(Base):
    __tablename__ = "schedules"

    id = Column(String(36), primary_key=True)
    description = Column(Text, nullable=False)

    date_start = Column(DateTime(timezone=True), nullable=False)
    date_end = Column(DateTime(timezone=True), nullable=True)

    time_start = Column(DateTime(timezone=True), nullable=False)
    time_end = Column(DateTime(timezone=True), nullable=False)

    # doctors = relationship("UserTable", back_populates="schedules")


Base.metadata.create_all(engine)

class ScheduleTable:
    id: str
    description: str
    date_request: str
    date_end: str
    time_start: str
    time_end: str
    # doctors: User

    class Config:
        orm_mode=True

    @staticmethod
    def from_model_table(schedulte_table: ScheduleTable):
        return Reservation(id=schedulte_table.id,
                    description=schedulte_table.description,
                    date_request=schedulte_table.date_request,
                    date_end=schedulte_table.date_end,
                    time_start=schedulte_table.time_start,
                    time_end=schedulte_table.time_end,
                    # doctors=schedulte_table.doctors
                    )