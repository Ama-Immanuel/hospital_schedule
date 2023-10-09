from typing import Annotated

from fastapi import APIRouter, Depends

import controller
import middleware
import shared
from dto import UserResponse, UserRequest
from model import User
from shared import IResponseBase, responses

route_schedule = APIRouter(
    prefix="/api/v1/schedule",
    tags=["Schedule"]
)


@route_schedule.post("/request", response_model=IResponseBase, responses=responses)
async def request(request):
    return shared.success_response(data=controller.requestSchedule)


@route_schedule.patch("/confirm", response_model=IResponseBase, responses=responses)
async def confirm(request):
    return shared.success_response(data=controller.confirmSchedule(request))


@route_schedule.patch("/reject", response_model=IResponseBase, responses=responses)
async def reject(request):
    return shared.success_response(data=controller.rejectSchedule(request))

@route_schedule.patch("/cancel", response_model=IResponseBase, responses=responses)
async def cancel(request):
    return shared.success_response(data=controller.requestSchedule(request))
