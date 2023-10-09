from pydantic import BaseModel

class ResponseGetAllNurses(BaseModel):
    name:str
    phone_number:str
    email:str
