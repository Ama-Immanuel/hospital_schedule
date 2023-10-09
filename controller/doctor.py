# from shared import *
# from dto import ResponseGetAllNurses

async def getAllNurses(role: str):
    if role == "doctor":  
        return success_response(data=ResponseGetAllNurses(name="test", phone_number="test", email="test"))
    raise ExceptionBadRequest("500000")