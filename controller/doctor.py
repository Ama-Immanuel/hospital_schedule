from config import cfg
from model import *
from dto import *
from typing import List
from utils.db import session
from model import ROLE_PATIENT,ROLE_NURSE

def fetchNurses() -> List[GetNursesResponses]:
    nurse_query = session.query(UserTable)
    nurses: UserTable =  nurse_query.filter(UserTable.role == ROLE_NURSE).all()
    
    responses:List[GetNursesResponses] = []

    i = 0
    for n in nurses:
        i += 1
        responses.append(GetNursesResponses(name=n.name, phone_number=n.phone_number, email=n.email))

    return responses

def fetchPatients() -> List[GetNursesResponses]:
    nurse_query = session.query(UserTable)
    nurses: UserTable =  nurse_query.filter(UserTable.role == ROLE_PATIENT).all()
    
    responses:List[GetNursesResponses] = []

    i = 0
    for n in nurses:
        i += 1
        responses.append(GetNursesResponses(name=n.name, phone_number=n.phone_number, email=n.email))

    return responses