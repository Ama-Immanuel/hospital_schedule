from config import cfg
from model import *
from dto import *
from typing import List
from utils.db import session
from model import ROLE_PATIENT,ROLE_NURSE, ROLE_DOCTOR

def fetchNurses() -> List[GetNursesResponses]:
    user_query = session.query(UserTable)
    nurses: UserTable =  user_query.filter(UserTable.role == ROLE_NURSE).all()
    
    responses:List[GetNursesResponses] = []

    i = 0
    for n in nurses:
        i += 1
        responses.append(GetNursesResponses(name=n.name, phone_number=n.phone_number, email=n.email))

    return responses

def fetchPatients() -> List[GetPatientsResponses]:
    user_query = session.query(UserTable)
    users: UserTable =  user_query.filter(UserTable.role == ROLE_PATIENT).all()
    
    responses:List[GetPatientsResponses] = []

    for u in users:
        responses.append(GetPatientsResponses(name=u.name, phone_number=u.phone_number))
    
    return responses

def fetchDoctors()->List[GetDoctorsResponses]:
    user_query = session.query(UserTable)
    users: UserTable =  user_query.filter(UserTable.role == ROLE_DOCTOR).all()
    
    responses:List[GetDoctorsResponses] = []

    for u in users:
        responses.append(GetDoctorsResponses(name=u.name, phone_number=u.phone_number, email=u.email, code=u.code))

    return responses