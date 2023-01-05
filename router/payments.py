from fastapi import APIRouter
from typing import List
from dao.Payments import PaymentsDao

from models.payment import Payment_model

router = APIRouter(prefix='/payments', tags=['payments'])

@router.get('/all', response_model=List[Payment_model])
async def getPayments():
    return  PaymentsDao.getAllPayments()

@router.post('/new', response_model = Payment_model, response_model_include={'check_number'})
async def addPayment(payment : Payment_model):
    return payment