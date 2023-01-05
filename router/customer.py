from models.customer import CustomerModel
from fastapi import APIRouter, status
from typing import List
from fastapi.encoders import jsonable_encoder
from dao.customersDao import CustomersDao
from dto.Customer import Customer

router = APIRouter(prefix='/customer', tags=['customer'])

@router.get(
  '/all', 
  response_model=List[CustomerModel],
  response_model_exclude_none=True,
  response_model_include={"contactLastName", "contactFirstName", "phone", "salesRepEmployeeNumber", "creditLimit"})
async def getCustomer():
    results = CustomersDao.getAllCustomers()
    a = 0
    return results

@router.post('/new', response_model=CustomerModel, response_model_include={'customerNumber'}, status_code=status.HTTP_201_CREATED)
async def addCustomer(customer : CustomerModel):
  return customer
