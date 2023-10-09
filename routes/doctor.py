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
async def getAllNurses():
    return shared.success_response(data=controller.fetchNurses())

@route_doctor.get("/get/patients", response_model=IResponseBase[List[GetPatientsResponses]], responses=responses)
async def getAllPatients():
    return shared.success_response(data=controller.fetchPatients())

@route_doctor.get("/get/doctors", response_model=IResponseBase[List[GetDoctorsResponses]], responses=responses)
async def getAllDoctors():
    return shared.success_response(data=controller.fetchDoctors())
