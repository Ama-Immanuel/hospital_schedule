from utils.db import session
from model import ROLE_DOCTOR,ROLE_NURSE
from model import *
from dto import *
from utils import create_password_hash
import uuid

def addNurse(request:UserRequest):
    user_query = session.query(UserTable)
    found_user = user_query.filter(UserTable.email == request.email).first()
    if found_user is None:
        new_user = UserTable(email=request.email,
                          id=uuid.uuid4(),
                          name=request.name,
                          password=create_password_hash(request.password),
                          phone_number=request.phone_number,
                          role=ROLE_NURSE,)
        session.add(new_user)
        session.commit()
        
        return new_user
    

def addDoctor(request:UserRequest):
    user_query = session.query(UserTable)
    found_user = user_query.filter(UserTable.email == request.email).first()
    if found_user is None:
        new_user = UserTable(email=request.email,
                          id=uuid.uuid4(),
                          name=request.name,
                          password=create_password_hash(request.password),
                          phone_number=request.phone_number,
                          role=ROLE_DOCTOR,)
        session.add(new_user)
        session.commit()
        return new_user

    