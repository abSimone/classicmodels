from models.employee import EmployeeModel
from fastapi import APIRouter
from typing import List
from dao.EmployeeDao import EmployeeDao
from dto.Employee import Employee

router = APIRouter(prefix='/employee', tags=['employee'])

@router.get('/all',  
  response_model=List[EmployeeModel],
  response_model_exclude_none=True,
  response_model_include={"lastName", "firstName", "email"}
  )
async def getEmployees():
    return EmployeeDao.getAllEmployees()

@router.post('/new')
async def addEmployee(empolyee :EmployeeModel):
  return empolyee