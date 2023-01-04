from fastapi import APIRouter

from dao.Payments import PaymentsDao

from models.payment import Payment_model

router = APIRouter(prefix='/payments', tags=['payments'])

@router.get('/all')
async def getPayments():
    return {'payments' : PaymentsDao.getAllPayments()}

@router.post('/new', response_model = Payment_model)
async def addPayment(payment : Payment_model):
    return payment