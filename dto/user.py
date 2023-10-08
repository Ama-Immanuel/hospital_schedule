from pydantic import BaseModel

class ResponseUser(BaseModel):
    name:str
    phone_number:str
    password:str
    email:str
    code:str
    role:str
