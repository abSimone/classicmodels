
from fastapi import FastAPI
from typing import List

from models.office import OfficeModel
import router.orders as orders

from dao.productDao import Product
from dao.productLinesDao import ProductLines
from dao.Payments import PaymentsDao
from dao.orderDetailDao import orderDetails
from dao.officesDao import OfficeDao
from dao.EmployeeDao import EmployeeDao
from dao.customersDao import CustomersDao

app = FastAPI()

app.include_router(orders.router)

# ------ Gruppo 2 ------
@app.get('/products')
async def getProducts():
    return {'products' : Product.getAllProduct()}

@app.get('/productLines')
async def getProductLines():
    return {'productLines' : ProductLines.getAllProductLines()}

# ------ Gruppo 3 ------
@app.get('/payments')
async def getPayments():
    return {'payments' : PaymentsDao.getAllPayments()}

@app.get('/orderDetails')
async def getOrderDetails():
    return {'oDetails' : orderDetails.getAllOrdersDetails()}

# ------ Gruppo 1 + 4 ------
@app.get('/offices')
async def getOffices():
    return OfficeDao.getAllOffices()

@app.post('/offices/new', response_model=OfficeModel, response_model_include={"officeCode", "postalCode", "territory"})
async def addOffice(office : OfficeModel):
  return office

@app.get('/employee')
async def getEmployee():
    return {'employees' : EmployeeDao.getAllEmployees()}

@app.get('/customers')
async def getCustomers():
    return {'costomers' : CustomersDao.getAllCustomers()}

