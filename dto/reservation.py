from pydantic import BaseModel

class reservationRequest(BaseModel):
    date_request:str
    date_request_at:str
    time_start:str
    time_end:str
    reason:str
    schedule_id:str

class reservationByNurseRequest(BaseModel):
    date_request:str
    date_request_at:str
    time_start:str
    time_end:str
    reason:str
    schedule_id:str
    patient_id:str
