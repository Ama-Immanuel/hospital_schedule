from fastapi import APIRouter

from dto import AuthResponse, LoginRequest
from shared import IResponseBase, responses

route_auth = APIRouter(
    prefix="/api/v1/auth",
    tags=["Auth"]
)


@route_auth.post("/login", response_model=IResponseBase[AuthResponse], responses=responses)
async def login(request: LoginRequest):
    pass


@route_auth.post("/register", response_model=IResponseBase[AuthResponse], responses=responses)
async def refresh_token():
    pass
