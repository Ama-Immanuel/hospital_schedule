from typing import Any

from dto import *


def login_process(req: LoginRequest) -> AuthResponse:
    user = authenticate_user(req.email, req.password)
    return AuthResponse(token="", refresh_token="", expired_at="")


def authenticate_user(username: str, password: str) -> Any:
    pass


def refresh_token_process():
    pass
