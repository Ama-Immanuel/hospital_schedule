from typing import Annotated

from fastapi import APIRouter, Depends

import controller
import middleware
import shared
from dto import UserResponse, UserRequest
from model import User
from shared import IResponseBase, responses

route_admin = APIRouter(
    prefix="/api/v1/admin",
    tags=["Admin"]
)


@route_admin.post("/add/nurse", response_model=IResponseBase[UserResponse], responses=responses)
async def add_nurse(request: UserRequest):
    return shared.success_response(data=controller.addNurse(request))


@route_admin.post("/add/doctor", response_model=IResponseBase[UserResponse], responses=responses)
async def add_doctor(request: UserRequest):
    return shared.success_response(data=controller.addDoctor(request))
