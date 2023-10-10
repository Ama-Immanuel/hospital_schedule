class ScheduleResponse:
    description:str
    # doctor_id:str
    date_start:str
    date_end:str
    time_start:str
    time_end:str


class GetSchedulesRequest:
    doctor_id:str
    date:str