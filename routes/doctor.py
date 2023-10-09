from fastapi import APIRouter
from dto import ResponseGetAllNurses
from shared import *
from controller import doctor

route_doctor = APIRouter(
    prefix="/api/v1/doctors",
    tags=["Doctors"]
)

@route_doctor.patch("/getAllNurses", response_model=IResponseBase[ResponseGetAllNurses], responses=responses)
# doctor.getAllNurses