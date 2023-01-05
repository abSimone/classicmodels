from fastapi import APIRouter
from models.office import OfficeModel
from dao.officesDao import OfficeDao
from typing import List
from dto.Office import Office

router = APIRouter(prefix='/offices', tags=['offices'])

@router.get('/all',
    response_model = List[OfficeModel],
    response_model_exclude_none = True,
    # response_model_exclude = {'city', 'phone', 'addressLine1', 'addressLine2', 'state', 'country',  'postalCode', 'territory'},
    response_model_include = {'officeCode'})
async def getOffices():
    return OfficeDao.getAllOffices()

@router.post('/new')
async def addOffice(office : OfficeModel):
  return office