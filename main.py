import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from config import cfg
from routes import *
from shared import *

app = FastAPI()

app.add_exception_handler(ExceptionNotFound, exception_handler_not_found)
app.add_exception_handler(ExceptionInternalServerError, exception_handler_internal_server_error)
app.add_exception_handler(ExceptionUnauthorized, exception_handler_unauthorized)
app.add_exception_handler(ExceptionForbidden, exception_handler_forbidden)
app.add_exception_handler(ExceptionBadRequest, exception_handler_bad_request)


@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    return RedirectResponse('https://fastapi.tiangolo.com')


app.include_router(route_home)
app.include_router(route_auth)