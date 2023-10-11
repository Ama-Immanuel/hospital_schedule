from typing import Annotated

from fastapi import APIRouter, Depends

import controller
import middleware
import shared
from dto import UserResponse, UserRequest, GetNursesResponses, GetPatientsResponses, GetDoctorsResponses
from model import User
from shared import IResponseBase, responses
from typing import List

route_nurse = APIRouter(
    prefix="/api/v1/nurse",
    tags=["Nurse"]
)


@route_nurse.post("/reservation/request", response_model=IResponseBase, responses=responses)
async def request_reservation(request):
    return shared.success_response()


@route_nurse.patch("/reservation/confirm", response_model=IResponseBase, responses=responses)
async def confirm_reservation(request):
    return shared.success_response()

@route_nurse.patch("/reservation/reject", response_model=IResponseBase, responses=responses)
async def reject_reservation(request):
    return shared.success_response()

@route_nurse.patch("/reservation/cancel", response_model=IResponseBase, responses=responses)
async def cancel_reservation(request):
    return shared.success_response()

@route_nurse.get("/schedule/get", response_model=IResponseBase, responses=responses)
async def get_doctor_schedule(request):
    return shared.success_response()

@route_nurse.get("/get/patients", response_model=IResponseBase[List[GetPatientsResponses]], responses=responses)
async def get_all_patients():
    return shared.success_response(data=controller.fetchPatients())