from fastapi import APIRouter

from shared import IResponseBase

route_auth = APIRouter(
    prefix="/home",
    tags=["Home"]
)


@route_auth.post("/login", response_model=IResponseBase[dict])
async def login():
    pass
