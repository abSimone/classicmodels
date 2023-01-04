from models.customer import CustomerModel
from fastapi import APIRouter
from dao.customersDao import CustomersDao

router = APIRouter(prefix='/customer', tags=['customer'])

@router.get('/all')
async def getCustomer():
    return CustomersDao.getAllCustomers()

@router.post('/new')
async def addCustomer(customer : CustomerModel):
  return customer