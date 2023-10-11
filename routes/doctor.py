from fastapi import APIRouter, Depends
from dto import GetNursesResponses, GetPatientsResponses, GetDoctorsResponses, ScheduleResponse, ScheduleRequest
from shared import *

import controller
import shared
import middleware

from model import User, Schedule
from shared import IResponseBase, responses
from typing import List, Annotated
from model import ROLE_DOCTOR

route_doctor = APIRouter(
    prefix="/api/v1/doctors",
    tags=["Doctors"]
)

@route_doctor.get("/get/nurses", response_model=IResponseBase[List[GetNursesResponses]], responses=responses)
async def get_all_nurses():
    return shared.success_response(data=controller.fetchNurses())

@route_doctor.get("/get/patients", response_model=IResponseBase[List[GetPatientsResponses]], responses=responses)
async def get_all_patients():
    return shared.success_response(data=controller.fetchPatients())

@route_doctor.post("/schedule", response_model=IResponseBase[Schedule], responses=responses)
async def create_schedules(request:ScheduleRequest, current_user: Annotated[User, Depends(middleware.get_current_user)]):
    if(current_user.role == ROLE_DOCTOR):
        return shared.success_response(data=controller.createSchedule(request, current_user))
    else:
        return shared.error_response(message="try login as doctor", code="403001", error='only for doctor')

@route_doctor.patch("/reservation/confirm", response_model=IResponseBase, responses=responses)
async def confirm_reservation(request):
    return shared.success_response()

@route_doctor.patch("/reservation/reject", response_model=IResponseBase, responses=responses)
async def reject_reservation(request):
    return shared.success_response()

@route_doctor.patch("/reservation/cancel", response_model=IResponseBase, responses=responses)
async def cancel_reservation(request):
    return shared.success_response()

@route_doctor.patch("/reservation/assignNurse", response_model=IResponseBase, responses=responses)
async def assign_nurse_to_reservation():
    return shared.success_response()
