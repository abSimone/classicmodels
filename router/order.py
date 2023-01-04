from fastapi import APIRouter

from dao.ordersDao import Orders
from models.order import OrderModel

router = APIRouter(prefix='/orders', tags=['orders'])
# /orders/all
@router.get('')
async def getOrders():
  return {'orders' : Orders.getAllOrders()}

@router.post('/new', status_code=201)
async def addOrder(order : OrderModel):
  return {'detail' : 'success'}