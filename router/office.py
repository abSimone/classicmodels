from fastapi import APIRouter
from models.office import OfficeModel
from dao.officesDao import OfficeDao

router = APIRouter(prefix='/offices', tags=['offices'])

@router.get('/all')
async def getOffices():
    return OfficeDao.getAllOffices()

@router.post('/new')
async def addOffice(office : OfficeModel):
  return office