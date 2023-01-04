from models.employee import EmployeeModel
from fastapi import APIRouter
from dao.EmployeeDao import EmployeeDao

router = APIRouter(prefix='/employee', tags=['employee'])

@router.get('/all')
async def getEmployees():
    return EmployeeDao.getAllEmployees()

@router.post('/new')
async def addEmployee(empolyee :EmployeeModel):
  return empolyee