from config import cfg
from model import *
from dto import *
from typing import List
from utils.db import session
from model import ROLE_PATIENT,ROLE_NURSE, ROLE_DOCTOR

def fetchDoctors()->List[GetDoctorsResponses]:
    user_query = session.query(UserTable)
    users: UserTable =  user_query.filter(UserTable.role == ROLE_DOCTOR).all()
    
    responses:List[GetDoctorsResponses] = []

    for u in users:
        responses.append(GetDoctorsResponses(name=u.name, phone_number=u.phone_number, email=u.email, code=u.code))

    return responses