from fastapi import APIRouter, status
from models.office import OfficeModel
from dao.officesDao import OfficeDao
from typing import List

router = APIRouter(prefix='/offices', tags=['offices'])


@router.get(
    '/all',
    response_model=List[OfficeModel],
    response_model_exclude_none=True,
    response_model_exclude={'officeCode'})
async def getOffices():
    return OfficeDao.getAllOffices()


@router.post(
    '/new',
    response_model=OfficeModel,
    response_model_include={'officeCode'}, status_code=status.HTTP_201_CREATED
)
async def addOffice(office: OfficeModel):
    return office
