from models.customer import CustomerModel
from fastapi import APIRouter
from typing import List
from dao.customersDao import CustomersDao
from dto.Customer import Customer

router = APIRouter(prefix='/customer', tags=['customer'])

@router.get(
  '/all', 
  response_model=List[CustomerModel], 
  response_model_exclude={'contactFirstName'},
  response_model_include={'contactLastName'})
async def getCustomer():
    return CustomersDao.getAllCustomers()

@router.post('/new')
async def addCustomer(customer : CustomerModel):
  return customer
