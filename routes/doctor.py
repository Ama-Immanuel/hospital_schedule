from fastapi import APIRouter
from dto import GetNursesResponses, GetPatientResponses
from shared import *

import controller
import shared

from shared import IResponseBase, responses
from typing import List

route_doctor = APIRouter(
    prefix="/api/v1/doctors",
    tags=["Doctors"]
)

@route_doctor.get("/getAllNurses", response_model=IResponseBase[List[GetNursesResponses]], responses=responses)
async def getAllNurses():
    return shared.success_response(data=controller.fetchNurses())

@route_doctor.get("/getAllPatient", response_model=IResponseBase[List[GetPatientResponses]], responses=responses)
async def getAllPatient():
    return shared.success_response(data=controller.fetchPatients())
