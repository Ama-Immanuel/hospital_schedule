from pydantic import BaseModel


class AuthResponse(BaseModel):
    token: str
    refresh_token: str
    expired_at: int

class LoginRequest(BaseModel):
    email: str
    password: str
    role: str
    