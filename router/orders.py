from fastapi import APIRouter

from dao.ordersDao import Orders

router = APIRouter(prefix='/orders', tags=['orders'])
# /orders/all
@router.get('/all')
async def getOrders():
  return {'orders' : Orders.getAllOrders()}