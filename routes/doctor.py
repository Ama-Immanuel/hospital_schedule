from fastapi import APIRouter

route_doctor = APIRouter(
    prefix="/api/v1/doctors",
    tags=["Doctors"]
)
