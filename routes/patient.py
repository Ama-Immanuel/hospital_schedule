from typing import Annotated

from fastapi import APIRouter, Depends

import controller
import middleware
import shared
from dto import UserResponse, UserRequest
from model import User
from shared import IResponseBase, responses

route_patient = APIRouter(
    prefix="/api/v1/patient",
    tags=["Patient"]
)


@route_patient.post("/reservation/request", response_model=IResponseBase, responses=responses)
async def request_reservation(request):
    pass


@route_patient.patch("/reservation/cancel", response_model=IResponseBase, responses=responses)
async def cancel_reservation(request):
    pass

@route_patient.get("/schedule/get", response_model=IResponseBase, responses=responses)
async def get_doctor_schedule():
    pass

@route_patient.get("/doctor/getAll", response_model=IResponseBase, responses=responses)
async def get_all_doctors():
    pass

