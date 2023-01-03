from fastapi import FastAPI

from dao.ordersDao import Orders
from dao.productDao import Product
from dao.productLinesDao import ProductLinesDao
from dao.Payments import PaymentsDao
from dao.orderDetailsDao import orderDetailsDao
from dao.officesDao import OfficeDao
from dao.EmployeeDao import EmployeeDao
from dao.customersDao import CustomersDao

app = FastAPI()

@app.get('/orders')
async def getOrders():
  return {'orders' : Orders.getAllOrders()}

@app.get('/products')
async def getProducts():
    return {'products' : Product.getAllProduct()}

@app.get('/productLines')
async def getProductLines():
    return {'productLines' : ProductLinesDao.getAllProductLines()}

@app.get('/payments')
async def getPayments():
    return {'payments' : PaymentsDao.getAllPayments()}

@app.get('/orderDetails')
async def getOrderDetails():
    return {'oDetails' : orderDetailsDao.getAllOrdersDetails()}

@app.get('/offices')
async def getOffices():
    return {'offices' : OfficeDao.getAllOffices()}

@app.get('/employee')
async def getEmployee():
    return {'employees' : EmployeeDao.getAllEmployees()}

@app.get('/customers')
async def getCustomers():
    return {'costomers' : CustomersDao.getAllCustomers()}
