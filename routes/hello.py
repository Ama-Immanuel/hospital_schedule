from fastapi import APIRouter

from dto import ResponseHello
from shared import IResponseBase, success_response

route_home = APIRouter(
    prefix="/home",
    tags=["Home"]
)


@route_home.get("/hello/{name}", response_model=IResponseBase[ResponseHello])
async def say_hello(name: str):
    return success_response(data=ResponseHello(name=name, message=f"Hello {name}"))
