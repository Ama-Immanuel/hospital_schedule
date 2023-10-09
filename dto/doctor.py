from pydantic import BaseModel

class GetNursesResponses(BaseModel):
    name:str
    phone_number:str
    email:str

class GetPatientResponses(BaseModel):
    name:str
    email:str
