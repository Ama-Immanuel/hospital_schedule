from fastapi import APIRouter
from dto import GetNursesResponses, GetPatientsResponses, GetDoctorsResponses
from shared import *

import controller
import shared

from shared import IResponseBase, responses
from typing import List

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

@route_doctor.patch("/reservation/assignNurse", response_model=IResponseBase, responses=responses)
async def assign_nurse_to_reservation():
    return shared.success_response()
