from typing import Any

import fastapi
from fastapi import HTTPException, status
from pydantic import BaseModel
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from shared import error_response


# 404
class ExceptionNotFound(BaseModel, HTTPException):
    code: int
    message: str
    cause: Any


def exception_handler_not_found(request: Request, exc: ExceptionNotFound):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=error_response(
        error=exc.cause,
        code=exc.code,
        message=exc.message
    ))


# 400
class ExceptionBadRequest(BaseModel, HTTPException):
    code: int
    message: str
    cause: Any


def exception_handler_bad_request(request: Request, exc: ExceptionBadRequest):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=error_response(
        error=exc.cause,
        code=exc.code,
        message=exc.message
    ))


# 500
class ExceptionInternalServerError(BaseModel, HTTPException):
    code: int
    message: str
    cause: Any


def exception_handler_internal_server_error(request: Request, exc: ExceptionInternalServerError):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=error_response(
        error=exc.cause,
        code=exc.code,
        message=exc.message
    ))


# 401
class ExceptionUnauthorized(BaseModel, HTTPException):
    code: int
    message: str
    cause: Any


def exception_handler_unauthorized(request: Request, exc: ExceptionUnauthorized):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=error_response(
        error=exc.cause,
        code=exc.code,
        message=exc.message
    ))


# 403
class ExceptionForbidden(BaseModel, HTTPException):
    code: int
    message: str
    cause: Any


def exception_handler_forbidded(request: Request, exc: ExceptionForbidden):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=error_response(
        error=exc.cause,
        code=exc.code,
        message=exc.message
    ))
