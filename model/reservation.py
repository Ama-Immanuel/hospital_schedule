from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.orm import declarative_base
from utils.db import engine

Base = declarative_base()


class ReservationTable(Base):
    __tablename__ = "reservations"

    id = Column(String(36), primary_key=True)
    queue_number = Column(String(255), nullable=False)

    date_request = Column(DateTime(timezone=True), nullable=False)
    date_request_at = Column(DateTime(timezone=True), nullable=True)

    time_start = Column(DateTime(timezone=True), nullable=False)
    time_end = Column(DateTime(timezone=True), nullable=False)

    status = Column(String(20), nullable=False)
    reason = Column(Text, nullable=False)

    # schedule_id = Column(String(26), nullable=False)
    # patient_id = Column(String(26), nullable=False)
    # nurse_id = Column(String(26), nullable=False)


Base.metadata.create_all(engine)

class Reservation:
    id: str
    queue_number: str
    date_request: str
    date_request_at: str
    time_start: str
    time_end: str
    status: str
    reason: str
    

    @staticmethod
    def from_model_table(reservation_table: ReservationTable):
        return Reservation(id=reservation_table.id,
                    queue_number=reservation_table.queue_number,
                    date_request=reservation_table.date_request,
                    date_request_at=reservation_table.date_request_at,
                    time_start=reservation_table.time_start,
                    time_end=reservation_table.time_end,
                    status=reservation_table.status,
                    reason=reservation_table.reason,
                   )